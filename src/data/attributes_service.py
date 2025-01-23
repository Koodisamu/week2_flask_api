import psycopg2
from psycopg2.extras import RealDictCursor
from config import config
import json

def db_get_attributes():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'SELECT * FROM attributes;'
        cursor.execute(SQL)
        data = cursor.fetchall()
        cursor.close()
        return json.dumps({"attribute_list": data})
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_get_attribute_by_id(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'SELECT * FROM attributes where id = %s;'
        cursor.execute(SQL, (id,))
        row = cursor.fetchone()
        cursor.close()
        return json.dumps(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_create_attribute(name, desc, value, person_id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'INSERT INTO attributes (attribute_name, attribute_description, attribute_value, person_id) VALUES (%s, %s, %s, %s);'
        cursor.execute(SQL, (name, desc, value, person_id))
        con.commit()
        result = {"success": "created attribute name: %s " % name}
        cursor.close()
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


def db_update_attribute(id, name, desc, value, person_id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'UPDATE attributes SET attribute_name = %s, attribute_description = %s, attribute_value = %s, person_id = %s WHERE id = %s;'
        cursor.execute(SQL, (name, desc, value, person_id, id))
        con.commit()
        cursor.close()
        result = {"success": "updated attribute id: %s " % id}
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_delete_attribute(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'DELETE FROM attributes WHERE id = %s;'
        cursor.execute(SQL, (id,))
        con.commit()
        cursor.close()
        result = {"success": "deleted attribute id: %s " % id}
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

