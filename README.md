
# University Management System

This project is a console-based Python application designed to manage a university's basic information about students and teachers. It showcases key object-oriented programming (OOP) concepts and methods in Python.

## Features
- Create a college and add students and teachers to it.
- List all students and teachers with relevant details.
- Demonstrates OOP concepts such as inheritance, encapsulation, and method overriding.

## Project Structure
- `Person`: Base class with shared attributes like name, roll number, and mobile.
- `Student` and `Teacher`: Derived classes extending `Person` with specific attributes (branch and subject).
- `College`: Main class responsible for managing collections of students and teachers.

## Techniques and Modules Used
1. **Object-Oriented Programming (OOP)**:
   - **Inheritance**: Enables `Student` and `Teacher` to inherit attributes and methods from `Person`.
   - **Encapsulation**: Classes group related data and functions together, providing a modular design.
   - **Method Overriding**: The derived classes (`Student`, `Teacher`) extend the base class `Person`.

2. **Built-in Python Data Structures**:
   - Lists are used to store students and teachers within the `College` class.

## Usage

### Example
Here's how you can use the classes:

```python
from university_management import College, Student, Teacher

# Create a college instance
college = College("Tech University")

# Add students
student1 = Student("Alice", "S001", "1234567890", "Computer Science")
student2 = Student("Bob", "S002", "0987654321", "Electrical Engineering")
college.add_student(student1)
college.add_student(student2)

# Add teachers
teacher1 = Teacher("Dr. Smith", "T001", "1122334455", "Physics")
teacher2 = Teacher("Dr. Jones", "T002", "6677889900", "Mathematics")
college.add_teacher(teacher1)
college.add_teacher(teacher2)

# List all students and teachers
print("Students in the College:")
college.list_students()
print("\nTeachers in the College:")
college.list_teachers()
```

### Installation
1. Clone the repository.
   ```bash
   git clone https://github.com/your-username/UniversityManagementSystem.git
   ```
2. Navigate to the project directory.
   ```bash
   cd UniversityManagementSystem
   ```
3. Run the script.
   ```bash
   python university_management.py
   ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

*This project was developed to enhance Python OOP skills and demonstrate practical applications in a university context.*
