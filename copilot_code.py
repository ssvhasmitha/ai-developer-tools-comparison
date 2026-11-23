# Student Marks Analyzer
# This program calculates statistics, grades, and pass/fail counts.

# Function to assign grades
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Function to analyze marks
def analyze_marks(marks):
    # Handle empty list
    if len(marks) == 0:
        print("No marks available to analyze.")
        return

    # Validate marks
    for mark in marks:
        if mark < 0 or mark > 100:
            print("Error: Marks must be between 0 and 100.")
            return

    # Calculate statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Count pass and fail students
    passed = 0
    failed = 0

    for mark in marks:
        if mark >= 60:
            passed += 1
        else:
            failed += 1

    # Display results
    print("Student Marks Analyzer")
    print("-" * 25)
    print("Marks:", marks)
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Passed Students: {passed}")
    print(f"Failed Students: {failed}")

    print("\nGrades:")
    for mark in marks:
        print(f"Mark: {mark} -> Grade: {get_grade(mark)}")


# Sample input
marks = [95, 85, 75, 65, 45]

# Call the function
analyze_marks(marks)