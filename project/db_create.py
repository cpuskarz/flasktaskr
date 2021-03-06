from views import db
from models import Task
from datetime import date

#import sqlite3
#from _config import DATABASE_PATH

'''
with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, due_date TEXT NOT NULL, priority
            INTEGER NOT NULL, status INTEGER NOT NULL)""")

    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES("Finish this tutorial", "03/25/2015", 10, 1)'
    )

    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES ("Finish Real Python Course 2", "03/25/2015", 10, 1)'
    )
'''

db.create_all()

db.session.add(Task("Finish this tutorial", date(2015, 5, 11), 10, 1))
db.session.add(Task("Finish Real Python", date(2015, 5, 11), 8, 1))

db.session.commit()
