# Student Marks Analyzer

def analyze_marks(marks):

    # Handle empty list
    if len(marks) == 0:
        print("No marks available")
        return

    # Validate marks
    for mark in marks:
        if mark < 0 or mark > 100:
            print("Invalid marks")
            return

    # Calculate statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    passed = 0
    failed = 0

    # Count pass and fail
    for mark in marks:
        if mark >= 60:
            passed += 1
        else:
            failed += 1

    # Display results
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Passed:", passed)
    print("Failed:", failed)

    # Assign grades
    print("\nGrades:")
    for mark in marks:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "F"

        print(mark, ":", grade)


# Sample input
marks = [95, 85, 75, 65, 45]

analyze_marks(marks)