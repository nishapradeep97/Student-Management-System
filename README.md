
# Student Management System

## Project Overview

The Student Management System is a web-based application developed using Python Flask and MySQL. It helps users manage student records through a simple and responsive interface.

The application supports adding, viewing, updating, deleting, and searching student information.

## Application Screenshots

### Student Management Dashboard

![Student Management](screenshots/student-management.png)

### Edit Student Details

![Edit Student](screenshots/edit.png)


## Technologies Used

- Python
- Flask
- MySQL
- HTML5
- Bootstrap 5
- Jinja2
- MySQL Connector

## Features

### 1. Add Student
- Add new student details.
- Enter student name, age, and grade.
- Store student information in MySQL database.

### 2. View Students
- Display all student records.
- Show student ID, name, age, and grade.
- View records in a structured table.

### 3. Update Student
- Edit existing student information.
- Automatically display previously saved details.
- Update student records in the database.

### 4. Delete Student
- Delete student records using their ID.
- Confirmation message before deletion.

### 5. Search Student
- Search students by name.
- Search using student ID.
- Search using grade.
- Clear search to display all student records.

### 6. Responsive User Interface
- Designed using Bootstrap 5.
- Responsive layout.
- Simple and user-friendly interface.

## Project Structure

```text
Student-Management-System/
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates/
    ├── index.html
    └── edit.html
```

## Database Configuration

Create a MySQL database:

```sql
CREATE DATABASE StudentDB;

USE StudentDB;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR(20) NOT NULL
);
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/nishapradeep97/Student-Management-System.git
```

### Step 2: Navigate to Project Folder

```bash
cd Student-Management-System
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure MySQL

- Create the StudentDB database.
- Create the students table using the SQL query above.
- Configure your MySQL credentials in the application using environment variables.

### Step 6: Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## Application Workflow

1. Launch the Flask application.
2. Add student details through the form.
3. View all student records in the table.
4. Search students using name, ID, or grade.
5. Edit existing student information.
6. Delete unwanted student records.

## Future Enhancements

- Student login and authentication.
- Pagination for student records.
- Export student details to Excel or CSV.
- Improved form validation.
- Dashboard with student statistics.

## Author

Nisha Pradeep

GitHub: https://github.com/nishapradeep97
