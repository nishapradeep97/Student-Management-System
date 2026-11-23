
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, template_folder='templates')

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nishajijo@2017",
    database="StudentDB"
)

cursor = db.cursor()


# Display all students
@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)


# Add student
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']

    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)",
        (name, age, grade)
    )
    db.commit()

    return redirect(url_for('index'))


# Search student
@app.route('/search')
def search_student():
    keyword = request.args.get('keyword', '').strip()

    if keyword:
        search_value = f"%{keyword}%"

        cursor.execute(
            """
            SELECT * FROM students
            WHERE name LIKE %s
            OR grade LIKE %s
            OR CAST(id AS CHAR) LIKE %s
            """,
            (search_value, search_value, search_value)
        )
        students = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

    return render_template(
        'index.html',
        students=students,
        keyword=keyword
    )


# Edit student - Display existing details
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']

        cursor.execute(
            """
            UPDATE students
            SET name=%s, age=%s, grade=%s
            WHERE id=%s
            """,
            (name, age, grade, id)
        )

        db.commit()
        return redirect(url_for('index'))

    cursor.execute(
        "SELECT * FROM students WHERE id=%s",
        (id,)
    )

    student = cursor.fetchone()

    if student is None:
        return "Student not found", 404

    return render_template('edit.html', student=student)


# Delete student
@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
