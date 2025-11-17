'''
Kenneth Summers
Section Leader: Davranbek Kadirimbetov
Date: 17 November 2025
Mutable Discussion Week 13
'''

def load_grade_book(filename: str) -> dict[str, list[float]]:
    '''Loads grades from a CSV file into a grade book dictionary.

    Returns a dict mapping id -> list of grades.
    '''
    grade_book = {}

    with open(filename, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if not line: #skips blank lines
                continue

            parts = line.split(",")
            student_id = parts[0].strip() #keeps ID as string
            grades = [float(g) for g in parts[1:]] #converts the rest to floats

            if student_id in grade_book:
                #extends the existing list of grades
                grade_book[student_id].extend(grades)
            else:
                #creates a new entry
                grade_book[student_id] = grades

    return grade_book

def add_to_grade_book(filename: str, grade_book: dict[str, list[float]]) -> dict[str, list[float]]:
    '''Adds grades from filename into an existing grade_book dictionary.
    Uses the same CSV format as load_grade_book.
    Returns the updated grade_book.
    '''
    with open(filename, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            student_id = parts[0].strip()
            grades = [float(g) for g in parts[1:]]

            if student_id in grade_book:
                grade_book[student_id].extend(grades)
            else:
                grade_book[student_id] = grades

    return grade_book