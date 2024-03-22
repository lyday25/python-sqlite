import sqlite3 as sql
def init_db():
    connection = sql.connect('data.db')

    with open('sqlschema.sql') as f:
       connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO applications (app_name, email, job_title, job_description) VALUES (?, ?, ?, ?)",
            ('Laide', 'bal@yahoo.com', 'data curator', 'data gathering and data preservation')
            )
    
    cur.execute("INSERT INTO applications (app_name, email, job_title, job_description) VALUES (?, ?, ?, ?)",
            ('Tola', 'tolareg@gmail.com', 'data analyst', 'data cleaning and data visualisation')
            )
    cur.execute("INSERT INTO applications (app_name, email, job_title, job_description) VALUES (?, ?, ?, ?)",
            ('Bukola', 'bukky@yahoo.com', 'system administration', 'software and hardware configuration and maintenance')
            )



        
    connection.commit()
    connection.close()
    print('Records posted into the database.')
        
init_db()     
        