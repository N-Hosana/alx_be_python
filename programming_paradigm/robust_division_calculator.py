import sys

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        # Remove the trailing period from the result message
        return f"The result of the division is {numerator / denominator}"
    except ValueError:
        return "Error: Please enter numeric values only."

def main():
    if len(sys.argv) != 3:
        print("Usage: python robust_division_calculator.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
