#!/usr/bin/env python3
#Write `tools/jsonpick.py` that reads stdin JSON, prints one field (arg), exits non-zero on error. Add two sample invocations in README.
import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="Pick and print a field from a stdin JSON object.")
    parser.add_argument("field", help="The key to extract.")
    args = parser.parse_args()

    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, TypeError):
        print("Error: Invalid JSON input.", file=sys.stderr)
        sys.exit(1)

    if isinstance(data, dict) and args.field in data:
        value = data[args.field]
        print(json.dumps(value))
    else:
        print(f"Error: Field '{args.field}' not found.", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()