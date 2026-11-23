# Student Marks Analyzer
# This program analyzes a list of student marks.

PASS_MARK = 60  # Minimum mark needed to pass


def is_valid(marks):
    """Return True if every mark is a number between 0 and 100."""
    for mark in marks:
        if not isinstance(mark, (int, float)) or mark < 0 or mark > 100:
            return False
    return True


def get_grade(mark):
    """Return the grade letter for a single mark."""
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


def count_pass_fail(marks):
    """Return (number passed, number failed)."""
    passed = 0
    failed = 0
    for mark in marks:
        if mark >= PASS_MARK:
            passed += 1
        else:
            failed += 1
    return passed, failed


def analyze_marks(marks):
    """Analyze the marks and display the results."""
    # Step 1: Handle an empty list
    if len(marks) == 0:
        print("No marks to analyze. The list is empty.")
        return

    # Step 2: Validate the marks
    if not is_valid(marks):
        print("Error: All marks must be numbers between 0 and 100.")
        return

    # Step 3: Calculate the statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    passed, failed = count_pass_fail(marks)

    # Step 4: Display the results
    print("=" * 30)
    print("    STUDENT MARKS ANALYZER")
    print("=" * 30)
    print("Marks entered :", marks)
    print()
    print(f"Average mark  : {average:.2f}")
    print(f"Highest mark  : {highest}")
    print(f"Lowest mark   : {lowest}")
    print()
    print(f"Passed        : {passed}")
    print(f"Failed        : {failed}")
    print()
    print(f"{'Student':<10}{'Mark':<8}{'Grade'}")
    print("-" * 30)
    for number, mark in enumerate(marks, start=1):
        print(f"{number:<10}{mark:<8}{get_grade(mark)}")
    print("=" * 30)


# Main program
student_marks = [95, 85, 75, 65, 45]
analyze_marks(student_marks)