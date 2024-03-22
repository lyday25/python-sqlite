import sqlite3
from flask import Flask, render_template
from flask import Flask, render_template, request, url_for, flash, redirect,abort

# ...
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

# ...

@app.route('/new/', methods=('GET', 'POST'))
def new():
    return render_template('create.html')

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM applications').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# ...

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM applications WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

# ...

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        app_name = request.form['app_name']
        email = request.form['email']
        job_title = request.form['job_title']
        job_description = request.form['job_description']

        if not app_name:
            flash('app_name is required!')

        elif not email:
            flash('email is required!')
            
        elif not job_title:
            flash('job_title is required!')
            
        elif not job_description:
            flash('job_description is required!')        

        else:
            conn = get_db_connection()
            conn.execute('UPDATE applications SET app_name = ?, email = ?, job_title = ?, job_description =?'
                         ' WHERE id = ?',
                         (app_name, email, job_title, job_description, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        app_name = request.form['app_name']
        email = request.form['email']
        job_title = request.form['job_title']
        job_description = request.form['job_description']

        if not app_name:
            flash('Name is required!')
        elif not email:
            flash('Email is required!')
        elif not job_title:
            flash('Job title is required!')
            
        elif not job_description:
            flash('Job description is required!')
            
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO applications (app_name, email, job_title, job_description) VALUES (?, ?, ?, ?)',
                         (app_name, email, job_title, job_description))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


# ...

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM applications WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was deleted successfully !'.format(post['app_name']))
    return redirect(url_for('index'))


if __name__ == '__main__':
      
       app.run(debug = True)
