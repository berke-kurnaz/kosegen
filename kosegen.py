import math

def calculate_diagonal(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Side lengths must be positive numbers.")
    return math.sqrt(width**2 + height**2)

def main():
    print("--- Diagonal Length Calculator ---")
    try:
        w = float(input("Enter the width (a): "))
        h = float(input("Enter the height (b): "))
        
        diagonal = calculate_diagonal(w, h)
        print(f"\nCalculated Diagonal Length: {diagonal:.2f}")
        
    except ValueError as e:
        if str(e) == "could not convert string to float":
            print("\nError: Please enter valid numerical values.")
        else:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()