# Collection-manipulator
# Student Data Organizer

## Project: Collection Manipulator

## Objective
A Python console program called **Student Data Organizer** that manages a collection of student records. The project applies intermediate-level Python concepts: string formatting and manipulation, collection data types (List, Tuple, Set, and Dictionary), mutability and immutability, type casting, and the `del` keyword.

---

## Requirements

### 1. String Formatting and Manipulation
- Gather and store student information (name, age, grade, subjects) using `input()`.
- Format the information for display in a user-friendly way.
- Demonstrate different string formatting methods (f-strings, `.format()`, and `%` formatting) when displaying student details.

### 2. Collection Data Types
- **List** — stores multiple student records and their information.
- **Tuple** — stores each student's unique and unchangeable information (student ID and date of birth).
- **Set** — manages and displays unique subjects offered across all students, ensuring no duplicates.
- **Dictionary** — organizes student data where keys are student IDs and values are dictionaries containing the student's name, age, grade, and list of subjects.

### 3. Mutability and Immutability
- Demonstrate the mutability of `List` by adding or modifying student details.
- Use the immutability of `Tuple` to handle each student's ID and date of birth, which must not change once set.

### 4. Type Casting and `del` Keyword
- Perform type casting where needed, such as converting user input strings to integers or floats (e.g., age).
- Use the `del` keyword to delete a student record from the main list based on student ID.

---

## Program Flow

### Welcome and Instructions
- Display a welcome message and an overview of the program's functionality.

### Student Data Collection
- Prompt the user to enter details for each student: name, age, grade, subjects (as a comma-separated string), student ID, and date of birth.
- Store the student's ID and date of birth as a tuple, add subjects to a set, and store each student's information in a dictionary. Add this dictionary to a list of all student records.

### Menu-Driven Options
| Option | Description |
|--------|-------------|
| 1. Add Student | Add a new student record. |
| 2. Display All Students | Display all student records using formatted output, listing the student ID, name, age, grade, and subjects. |
| 3. Update Student Information | Update specific mutable information, like age or subjects, of a selected student by ID. |
| 4. Delete Student | Remove a student record using student ID via `del`. |
| 5. Display Subjects Offered | Display all unique subjects offered by students, using a set to ensure no duplicates. |
| 6. Exit | Thank the user for using the Student Data Organizer and display an exit message. |

### Exit Message
- Thank the user for using the Student Data Organizer and display an exit message.

---

## Example Console Interaction

```
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 1

Enter student details:
Student ID: 101
Name: Alice
Age: 20
Grade: B+
Date of Birth (YYYY-MM-DD): 2002-05-14
Subjects (comma-separated): Math, Science, English

Student added successfully!

Select an option:
1. Add Student
2. Display All Students
...

--- Display All Students ---
Student ID: 101 | Name: Alice | Age: 20 | Grade: B+ | Subjects: Math, Science, English
...

Select an option:
...
```

---

## Assumptions
- Student IDs are assumed to be unique integers; the program does not allow duplicate IDs when adding a new student.
- Age is captured as user input (string) and type-cast to an integer before being stored.
- Subjects are entered as a comma-separated string and converted into a set to remove duplicates before being stored in the student's dictionary.
- Date of birth is entered in `YYYY-MM-DD` string format and stored as-is inside the immutable tuple (no date validation beyond basic format checking).
- "Update Student Information" only allows editing of mutable fields (age, grade, subjects); the student ID and date of birth tuple are treated as immutable and cannot be changed after creation.
- If a user attempts to delete or update a student ID that doesn't exist, the program displays an appropriate error message and returns to the main menu instead of crashing.
- Invalid menu input (non-numeric or out-of-range choice) is handled gracefully with a re-prompt rather than a program crash.

---

## How to Run
1. Ensure Python 3.x is installed.
2. Clone this repository:
   ```
   git clone <your-repository-url>
   ```
3. Navigate to the project directory:
   ```
   cd student-data-organizer
   ```
4. Run the program:
   ```
   python student_data_organizer.py
   ```
5. Follow the on-screen menu to add, view, update, delete, and inspect student records.

---

## Concepts Demonstrated
- **String Formatting:** f-strings, `.format()`, and `%`-style formatting used across different display functions.
- **List:** the master list of all student record dictionaries; supports adding and removing entries.
- **Tuple:** `(student_id, date_of_birth)` pairs stored as immutable identifiers for each student.
- **Set:** aggregated collection of all unique subjects offered, rebuilt from every student's subject list.
- **Dictionary:** each student's record (`name`, `age`, `grade`, `subjects`) keyed by student ID in a master dictionary/list structure.
- **Mutability vs. Immutability:** lists and dictionaries are mutated directly (add/update/delete); tuples remain fixed once created.
- **Type Casting:** `int()` used for age, `str.strip().split(',')` plus casting for subject lists.
- **`del` Keyword:** used explicitly to remove a student record from the list/dictionary by student ID.

---

## Notes for Submission
- All source code and this documentation are included in the GitHub repository.
- No code or content was copied from classmates or external sources; all logic is original.
- Please refer to the inline code comments for further implementation details.
