def get_grade(mark):
    """Returns a letter grade based on a single mark."""
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


def validate_marks(marks):
    """Checks if the list is valid and all marks are between 0 and 100."""
    # Check if the list is empty
    if not marks:
        print("Error: The marks list is empty.")
        return False

    # Check if every mark is within the valid range (0 to 100)
    for mark in marks:
        if mark < 0 or mark > 100:
            print(f"Error: Invalid mark '{mark}' found. Marks must be between 0 and 100.")
            return False

    return True


def analyze_marks(marks):
    """Calculates statistics, pass/fail counts, and prints the final report."""
    # Step 1: Validate input before doing any calculations
    if not validate_marks(marks):
        return

    # Step 2: Calculate basic statistics
    total_students = len(marks)
    average_mark = sum(marks) / total_students
    highest_mark = max(marks)
    lowest_mark = min(marks)

    # Step 3: Count passed/failed students and assign grades
    passed_count = 0
    failed_count = 0
    grades = []

    for mark in marks:
        if mark >= 60:
            passed_count += 1
        else:
            failed_count += 1

        grades.append(get_grade(mark))

    # Step 4: Display the results clearly
    print("=== Student Marks Analysis ===")
    print(f"Marks Entered : {marks}")
    print(f"Total Students: {total_students}")
    print("-" * 30)
    print(f"Average Mark  : {average_mark:.2f}")
    print(f"Highest Mark  : {highest_mark}")
    print(f"Lowest Mark   : {lowest_mark}")
    print("-" * 30)
    print(f"Passed (>=60) : {passed_count}")
    print(f"Failed (<60)  : {failed_count}")
    print("-" * 30)
    print("Student Grades:")
    for i in range(total_students):
        print(f"  Student {i + 1}: {marks[i]} -> Grade {grades[i]}")


# --- Main Execution ---
if __name__ == "__main__":
    sample_marks = [95, 85, 75, 65, 45]
    analyze_marks(sample_marks)