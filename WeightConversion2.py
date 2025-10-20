# File: weight_converter/cli.py

import argparse
from .converter import convert_weight

def main():
    parser = argparse.ArgumentParser(
        description="Convert weight between common units (kg, lb, g, oz, st)."
    )
    parser.add_argument(
        "--weight", type=float, required=True, help="The weight value to convert"
    )
    parser.add_argument(
        "--unit",
        type=str,
        required=True,
        choices=["kg", "lb", "g", "oz", "st"],
        help="The source unit (kg, lb, g, oz, st)",
    )
    parser.add_argument(
        "--round",
        type=int,
        default=2,
        help="Decimal precision to round the output (default: 2)",
    )

    args = parser.parse_args()

    try:
        results = convert_weight(args.weight, args.unit.lower(), args.round)
        print(f"\n{args.weight} {args.unit} is equivalent to:")
        for target_unit, value in results.items():
            print(f"  {value} {target_unit}")
    except Exception as e:
        print(f"Error: {e}")
