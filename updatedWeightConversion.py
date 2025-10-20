import argparse

def updatedWeightConversion(weight, unit):
    if unit == 'kg':
        converted = weight * 2.205
        print(f"{weight} kg is {round(converted, 1)} lbs.")
    elif unit == 'lb':
        converted = weight / 2.205
        print(f"{weight} lb is {round(converted, 2)} kg.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert weight between Kg and Lb.")
    parser.add_argument('--weight', type=float, required=True, help='Weight value to convert')
    parser.add_argument('--unit', type=str, required=True, choices=['kg', 'lb'], help='Input unit: "kg" or "lb"')

    args = parser.parse_args()
    updatedWeightConversion(args.weight, args.unit)
