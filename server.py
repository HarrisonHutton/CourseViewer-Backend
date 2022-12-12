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
        courses = db.get_dept_courses("CSE")
        return jsonify(courses)
    except:
        print("Error: Could not find courses")
        return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)