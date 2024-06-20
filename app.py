import data

from flask import Flask, jsonify

app = Flask(__name__)

# @app.route('/students/')
# def get_students():
#     passf

@app.route('/old_students/')
def get_old_students():
    old_students = []
    for item in data.students:
        if item['age'] > 20:
            old_students.append(item)
    return jsonify(old_students)

@app.route('/young_students/')
def get_young_students():
    young_students = []
    for item in data.students:
        if item['age'] < 20:
            young_students.append(item)
    return jsonify(young_students)


@app.route('/advance_students/')
def advance_students():
    advance_students = []
    for item in data.students:
        if item['age'] < 21 and item['grade'] == 'A':
            advance_students.append(item)
    return jsonify(advance_students)

@app.route('/student_names/')
def student_names():
    student_names = []
    for item in data.students:
        student_names.append({'first_name': item['first_name'], 'last_name': item['last_name']})
    return jsonify(student_names)



app.run(debug=True, port=5000)

