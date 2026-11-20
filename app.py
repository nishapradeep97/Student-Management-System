
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, template_folder='templates')

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="****",
    database="StudentDB"
)

cursor = db.cursor()

# Display students
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


# Delete student
@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
