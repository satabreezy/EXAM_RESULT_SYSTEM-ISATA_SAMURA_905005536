
# ---------------------------------------------------------------- Task 1
class Student:
    """A learner, identified by an anonymous ID (privacy-respecting)."""

    total_students = 0  # class attribute (shared by all students)

    def __init__(self, student_id, alias, level):
        self.student_id = student_id
        self.alias = alias          # nickname only, not a real name
        self.level = level          # e.g. "Year 1"
        Student.total_students += 1

    def update_level(self, new_level):
        """Instance method: promote/change the student's level."""
        self.level = new_level

    def display_info(self):
        """Instance method: show student details."""
        print(f"Student ID: {self.student_id} | Alias: {self.alias} | Level: {self.level}")


class Exam:
    """An exam for a course, with a maximum mark."""

    def __init__(self, exam_id, course, max_marks=100):
        self.exam_id = exam_id
        self.course = course
        self.max_marks = max_marks

    def display_info(self):
        print(f"Exam ID: {self.exam_id} | Course: {self.course} | Max marks: {self.max_marks}")


class Result:
    """Links a Student object to an Exam object with a score (object interaction)."""

    # Tuple of (minimum percentage, grade) - immutable grade bands (bonus: tuples)
    GRADE_BANDS = (
        (80, "A"),
        (70, "B"),
        (60, "C"),
        (50, "D"),
        (0, "F"),
    )

    def __init__(self, student, exam, score):
        self.student = student
        self.exam = exam
        self.score = score

    def percentage(self):
        """Instance method: score as a percentage of the exam's maximum."""
        return (self.score / self.exam.max_marks) * 100

    def grade(self):
        """Instance method: convert percentage to a letter grade."""
        pct = self.percentage()
        for minimum, letter in Result.GRADE_BANDS:
            if pct >= minimum:
                return letter

    def display_info(self):
        print(
            f"{self.student.student_id} ({self.student.alias}) | {self.exam.course} | "
            f"{self.score}/{self.exam.max_marks} | {self.percentage():.1f}% | Grade {self.grade()}"
        )

    # ------------------------------------------------------------ Task 3
    @classmethod
    def from_percentage(cls, student, exam, pct):
        """Class method: build a Result from a percentage instead of a raw score."""
        return cls(student, exam, pct / 100 * exam.max_marks)

    @staticmethod
    def is_valid_score(score, max_marks):
        """Static method: check a score is within 0 and max_marks."""
        return isinstance(score, (int, float)) and 0 <= score <= max_marks


# ---------------------------------------------------------------- Task 2
class ResultsManager:
    """Stores Result objects in ONE data structure: a dictionary.
    Key = (student_id, exam_id) tuple, Value = Result object."""

    def __init__(self):
        self.records = {}

    def add_record(self, student, exam, score):
        """Add a result to the dictionary after validating it."""
        if not Result.is_valid_score(score, exam.max_marks):
            print(f"Invalid score {score} for {exam.course}. Must be 0-{exam.max_marks}.")
            return False
        key = (student.student_id, exam.exam_id)
        self.records[key] = Result(student, exam, score)
        print(f"Added result for {student.student_id} in {exam.course}.")
        return True

    def display_records(self):
        """Loop through the dictionary and display every record."""
        if not self.records:
            print("No records yet.")
            return
        print("\n--- All Results ---")
        for result in self.records.values():
            result.display_info()

    def class_average(self, exam_id):
        """Average percentage for one exam."""
        pcts = [r.percentage() for (sid, eid), r in self.records.items() if eid == exam_id]
        return sum(pcts) / len(pcts) if pcts else 0


# ---------------------------------------------------------------- Demo
def main():
    print("=== Digital Exam & Results Management System ===\n")

    # Create objects
    s1 = Student("S001", "Mariama", "Year 1")
    s2 = Student("S002", "Abu", "Year 1")
    s3 = Student("S003", "Fatmata", "Year 2")
    e1 = Exam("E101", "Python Programming")
    e2 = Exam("E102", "Database Systems", 50)

    for obj in (s1, s2, s3, e1, e2):
        obj.display_info()

    # Store and interact through the manager (dictionary)
    manager = ResultsManager()
    print()
    manager.add_record(s1, e1, 85)
    manager.add_record(s2, e1, 67)
    manager.add_record(s3, e1, 45)
    manager.add_record(s1, e2, 38)
    manager.add_record(s2, e2, 120)  # invalid -> rejected

    # Class method: create a result from a percentage
    manager.records[(s3.student_id, e2.exam_id)] = Result.from_percentage(s3, e2, 72)

    manager.display_records()

    print(f"\nAverage for {e1.course}: {manager.class_average('E101'):.1f}%")
    s2.update_level("Year 2")
    s2.display_info()
    print(f"Total students created: {Student.total_students}")


if __name__ == "__main__":
    main()