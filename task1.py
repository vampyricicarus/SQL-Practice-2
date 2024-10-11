
import mysql.connector
db_name = "new_schema"
user = "root"
password = "Z3bEnn1%402024"
host = "localhost"

conn = mysql.connector("new_schema")
cursor = conn.cursor()

def add_member(id, name, age):
    cursor.execute("INSERT INTO members (id, name, age) VALUES (%s, %s, %s)", (id, name, age))
    cursor.commit

add_member(5, "John Doe", 21)

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    cursor.execute("INSERT INTO workout_session (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)", (member_id, date, duration_minutes, calories_burned))
    cursor.commit

add_workout_session(5, "2024-01-01", 23, 200)

def update_member_age(member_id, new_age):
    cursor.execute("UPDATE members (member_id, new_age) VALUES (%s, %s, %s)", (member_id, new_age))
    cursor.commit

update_member_age(5, 23)

def delete_workout_session(session_id):
    cursor.execute("DELETE workout_session (session_id) VALUES (%s)", (session_id))
    cursor.commit

delete_workout_session(3)

def get_members_in_age_range(start_age, end_age):
    cursor.execute("SELECT * BETWEEN members (start_age, end_age) VALUES (%s)", (start_age, end_age))
    cursor.commit

get_members_in_age_range(20, 25)

conn.close()