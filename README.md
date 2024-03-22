# python-sqlite
The project demonstrates Create, Read, Update and Delete (CRUD) operations using python flask and sqlite
This is CRUD Operations web based Flask Application with an Sql database
first create directory python-sqlite
$ cd python-sqlite
# now try to create a virtual; environment
$python3 -m venv venv
# now activate the virtual environment

$ Source venev/bin/activate
# now create the the sqlschema.sql to house the table creation for the projects
$ vi sqlschema.sql
DROP TABLE IF EXISTS applications;


CREATE TABLE applications (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  app_name TEXT NOT NULL,
  email TEXT NOT NULL,
  job_title TEXT NOT NULL,
  job_description TEXT NOT NULL
  
);

Now create another file to the initail db set up

$ vi init_db.py

import sqlite3 as sql
def init_db():
    connection = sql.connect('database.db')


    with open('sqlschema.sql') as f:
        connection.executescript(f.read())

        cur = connection.cursor()
        
        connection.commit()
        connection.close()
        print('Initialized the database.')
        
init_db()  


#Immediately this is done it creates the database.db in the target root directory

#Now we now need to install the Flask web framework using the command below


$pip install flask