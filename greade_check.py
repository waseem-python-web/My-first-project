# Grade Calculator Project
# Author: Waseem

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def main():
    print("===== Student Grade Calculator =====\n")

    # User input
    name = input("Enter your name:")
    
    try:
        marks = float(input("Enter your marks (0-100): "))
        
        if marks < 0 or marks > 100:
            print("Invalid marks! Please enter between 0 and 100.")
            return
        
        # Calculate grade
        grade = calculate_grade(marks)

        # Output
        print("\n=====Your Result =====")
        print(f"Your Name :{name}")
        print(f"Your Marks:{marks}")
        print(f"YOUR Grade:{grade}")

    except ValueError:
        print("Please enter valid numeric marks!")


# Run program
if __name__ == "__main__":
    main()