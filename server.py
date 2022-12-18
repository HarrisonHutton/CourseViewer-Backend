"""
Flask server to serve the course data from the MongoDB database to the Angular frontend.
"""
from flask import Flask, jsonify
from flask_cors import CORS

from database.CoursesDB import CoursesDB
from database.DatabaseEnum import DatabaseEnum

app = Flask(__name__)
CORS(app, origins=["http://localhost:4200"])

db = CoursesDB(DatabaseEnum.DEV)

@app.route('/api/courses')
def get_all_courses():
    try:
        courses = db.get_all_courses()
        return jsonify(courses)
    except:
        print("Error: Could not find courses")
        return jsonify({})

@app.route('/api/courses/<dpt_code>', methods=['GET'])
def get_dpt_courses(dpt_code):
    try:
        courses = db.get_dpt_courses(dpt_code)
        return jsonify(courses)
    except:
        print(f"Error: Could not find courses for department code: {dpt_code}")
        return jsonify({})

@app.route('/api/departments', methods=['GET'])
def get_departments():
    try:
        departments = db.get_all_departments()
        return jsonify(departments)
    except:
        print(f"Error: Could not find any departments")
        return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)