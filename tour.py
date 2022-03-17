
from flask import Flask, render_template

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tms'

mysql = MySQL(app)
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        details = request.form
        name = details['name']
        email = details['email']
        phone = details['phone']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contact(name, email, phone, password) VALUES (%s, %s, %d, %s)", (name, email, phone, password))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('tour.html')

if __name__ == '__main__':
    app.run()