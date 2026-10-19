# Digital Exam & Results Management System

PROG211 Object-Oriented Programming 1 – Education domain (Limkokwing University, Sierra Leone)

## Problem
Schools often record exam results on paper, which is slow and error-prone. This program records exam results and automatically calculates percentages, grades and class averages.

## How it aligns with Digital Public Goods (DPG) standards
- **Open-source:** Hosted on GitHub; anyone can use, study and improve it.
- **Inclusive and accessible:** Plain text, simple menus/output, runs on any low-spec computer with Python 3 and no internet or paid software.
- **Privacy-respecting:** No sensitive data is stored. Students are identified only by an anonymous ID and an alias – no real names, addresses, phone numbers or ID numbers.
- **Modular and reusable:** Separate classes (`Student`, `Exam`, `Result`, `ResultsManager`) can be reused for other schools or extended.

## OOP concepts used
| Task | Where |
|---|---|
| Classes, attributes, objects | `Student`, `Exam`, `Result` (Result links a Student and an Exam) |
| Data structure | One dictionary in `ResultsManager.records`, key = `(student_id, exam_id)` tuple |
| Instance methods | `display_info()`, `update_level()`, `percentage()`, `grade()` |
| Class method | `Result.from_percentage()` |
| Static method | `Result.is_valid_score()` |
| Tuples (bonus) | Grade bands `Result.GRADE_BANDS` and dictionary keys |

## How to run
```
python exam_results.py
```

## Example output
```
Added result for S001 in Python Programming.
Invalid score 120 for Database Systems. Must be 0-50.

--- All Results ---
S001 (Mariama) | Python Programming | 85/100 | 85.0% | Grade A
S002 (Abu) | Python Programming | 67/100 | 67.0% | Grade C

Average for Python Programming: 65.7%
```

## Licence
MIT
