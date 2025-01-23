from flask import Flask, request
from attributes_service import db_get_attributes, db_get_attribute_by_id, db_create_attribute, db_update_attribute, db_delete_attribute

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return {"index": True}

@app.route('/attributes', methods=['GET'])
def get_all_attribute():
    try:  
        return db_get_attributes()
    except:
        return {"error": "no data"}
    
@app.route('/attributes/<int:id>', methods=['GET'])
def get_attribute_by_id(id):
    try:
        return db_get_attribute_by_id(id)
    except:
        return {"error": "no person with id %s" % id}

@app.route('/attributes', methods=['POST'])
def create_attribute():
    try: 
        data = request.get_json()
        name = data['attribute_name']
        desc = data['attribute_description']
        value = data['attribute_value']
        person_id = data['person_id']
        db_create_attribute(name, desc, value, person_id)
        return {"success": "created attribute: %s" % name}
    except:
        return {"error": "error creating attribute"}

@app.route("/attributes/<int:id>", methods=['PUT'])
def update_attribute(id):
    try:
        data = request.get_json()
        name = data['attribute_name']
        desc = data['attribute_description']
        value = data['attribute_value']
        person_id = data['person_id']
        db_update_attribute(id, name, desc, value, person_id)
        return {"success": "updated attribute"}
    except:
        return {"error": "error updating attribute"}

@app.route('/attributes/<int:id>', methods=['DELETE'])
def delete_attribute(id):
    try:
        return db_delete_attribute(id)
    except:
        return {"error": "no such person"}
    

if __name__ == "__main__":
    app.run()