def list_habits(db):
    ret = []

    my_cursor = db.cursor()
    my_cursor.execute("SELECT * FROM habits")
    my_results = my_cursor.fetchall()

    for id, title, created_at, updated_at in my_results:
        ret.append({"id":id, "title":title})

    return ret

def get_one_habit(db, habit_id):
    my_cursor = db.cursor()

    sql = "SELECT * FROM habits WHERE id = %s"
    values = (habit_id,)
    my_cursor.execute(sql, values)
    id,title,created_at,updated_at = my_cursor.fetchone()
    
    return {"id":id, "title":title}

def create_habit(db, title):
    my_cursor = db.cursor()

    sql = "INSERT INTO HABITS (title, created_at, updated_at) VALUES (%s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
    values = (title,)
    my_cursor.execute(sql, values)
    
    db.commit()

def edit_habit(db, habit_id, new_title):
    my_cursor = db.cursor()

    sql = "UPDATE habits SET title = %s WHERE id = %s"
    values = (new_title, habit_id,)
    my_cursor.execute(sql, values)
    
    db.commit()

def delete_habit(db,habit_id):
    my_cursor = db.cursor()

    sql = "DELETE FROM habits WHERE id = %s"
    values = (habit_id,)
    my_cursor.execute(sql, values)
    
    db.commit()