#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["jsonschema[format]==4.26.0"]
# ///
"""Validate evidence structure and timestamps; no readiness or approval claims."""
import argparse
import json
from pathlib import Path
import sys

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit('Run: uv run tools/check-evidence.py <evidence.json>')

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path)
    args = parser.parse_args()
    if 'date-time' not in Draft202012Validator.FORMAT_CHECKER.checkers:
        sys.exit('Missing timestamp support; run through uv as documented.')
    schema = json.loads((ROOT / 'templates/shipping-evidence.schema.json').read_text())
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
    errors = list(validator.iter_errors(json.loads(args.record.read_text())))
    for error in errors:
        path = '/'.join(str(part) for part in error.absolute_path) or '$'
        print(f'FAIL: {path}: {error.validator}', file=sys.stderr)
    if errors:
        return 1
    print('PASS: evidence structure and timestamps; assertions unverified.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print(f'FAIL: cannot read JSON ({type(error).__name__})', file=sys.stderr)
        sys.exit(1)
