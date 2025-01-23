from flask import Flask, request
from person_service import db_get_persons, db_get_person_by_id, db_create_person, db_update_person, db_delete_person 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:samupostgres@localhost:5432/skillio'
db = SQLAlchemy(app)

@app.route("/", methods=["GET"])
def index():
    return {"index": True}

@app.route('/person', methods=['GET'])
def get_all_person():
    try:  
        return db_get_persons()
    except:
        return {"error": "no data"}

@app.route('/person/<int:id>', methods=['GET'])
def get_person_by_id(id):
    try:
        return db_get_person_by_id(id)
    except:
        return {"error": "no person with id %s" % id}

@app.route("/person", methods=['POST'])
def create_person():
    try: 
        data = request.get_json()
        username = data['name']
        age = data['age']
        student = data['student']
        db_create_person(username, age, student)
        return {"success": "created person: %s" % username}
    except:
        return {"error": "error creating person"}

@app.route("/person/<int:id>", methods=['PUT'])
def update_person(id):
    try:
        data = request.get_json()
        username = data['name']
        age = data['age']
        student = data['student']
        db_update_person(id, username, age, student)
        return {"success": "updated person"}
    except:
        return {"error": "error updating person"}

@app.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    try:
        return db_delete_person(id)
    except:
        return {"error": "no such person"}
    
@app.route('/attribute', methods=['GET'])
def get_all_attributes():
    return    

if __name__ == "__main__":
    app.run()
