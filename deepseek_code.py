# ============================================
# Student Marks Analyzer
# A beginner-friendly program to analyze marks
# ============================================

def validate_marks(marks):
    """
    Check that every mark is a number between 0 and 100.
    Returns True if all marks are valid, otherwise False.
    """
    for mark in marks:
        # Check the mark is a number (int or float)
        if not isinstance(mark, (int, float)):
            print(f"❌ Invalid mark '{mark}': not a number.")
            return False
        # Check the mark is between 0 and 100
        if mark < 0 or mark > 100:
            print(f"❌ Invalid mark {mark}: must be between 0 and 100.")
            return False
    return True


def calculate_average(marks):
    """Return the average of the marks list."""
    return sum(marks) / len(marks)


def calculate_highest(marks):
    """Return the highest mark."""
    return max(marks)


def calculate_lowest(marks):
    """Return the lowest mark."""
    return min(marks)


def count_pass_fail(marks, pass_mark=60):
    """
    Count how many students passed and failed.
    A student passes if their mark is >= pass_mark.
    Returns (passed_count, failed_count).
    """
    passed = 0
    failed = 0
    for mark in marks:
        if mark >= pass_mark:
            passed += 1
        else:
            failed += 1
    return passed, failed


def get_grade(mark):
    """
    Return a letter grade for a single mark.
    A: 90+   B: 80+   C: 70+   D: 60+   F: below 60
    """
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


def assign_grades(marks):
    """Return a list of grades matching the marks list."""
    grades = []
    for mark in marks:
        grades.append(get_grade(mark))
    return grades


def display_results(marks):
    """Print a clear summary of the analysis."""
    print("=" * 40)
    print("       STUDENT MARKS ANALYZER")
    print("=" * 40)
    print(f"Marks entered : {marks}")

    # Handle empty list case
    if len(marks) == 0:
        print("\n⚠️  No marks to analyze. Please enter at least one mark.")
        print("=" * 40)
        return

    # 1. Average, highest, lowest
    avg = calculate_average(marks)
    high = calculate_highest(marks)
    low = calculate_lowest(marks)

    print(f"\n📊 Statistics:")
    print(f"   Average : {avg:.2f}")
    print(f"   Highest : {high}")
    print(f"   Lowest  : {low}")

    # 2. Pass / Fail count
    passed, failed = count_pass_fail(marks)
    print(f"\n✅ Pass / ❌ Fail (pass mark = 60):")
    print(f"   Passed : {passed}")
    print(f"   Failed : {failed}")

    # 3. Grades
    grades = assign_grades(marks)
    print(f"\n🎓 Grades:")
    for i in range(len(marks)):
        print(f"   Student {i+1}: {marks[i]} -> Grade {grades[i]}")

    print("=" * 40)


# ============================================
# Main program
# ============================================
if __name__ == "__main__":
    # Sample input
    marks = [95, 85, 75, 65, 45]

    # Validate before analyzing
    if validate_marks(marks):
        display_results(marks)

    # Also test the empty-list case
    print("\n--- Testing empty list ---")
    display_results([])