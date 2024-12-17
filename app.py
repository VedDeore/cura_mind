from flask import Flask, render_template, request, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import models.prediction_model as prediction
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
p1 = ""
p2 = ""
p3 = ""
p4 = 0
pr1 = ""
pr2 = ""
pr3 = ""
pr4 = ""
pr5 = ""

app.secret_key = os.getenv('SECRET_KEY')

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
 
mysql = MySQL(app)

@app.route("/")
def index():
    if not session.get("username"):
        return redirect("/login")
    return render_template('dashboard.html')

@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM tbl_user WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('dashboard.html', msg = msg)
        else:
            msg = '<h5 style="color:red">Incorrect username / password</h5>'
    return render_template('index.html', msg = msg)

@app.route('/adminlogin', methods =['GET', 'POST'])
def adminlogin():
    msg = ''
    if request.method == 'POST' and 'adminusername' in request.form and 'adminpassword' in request.form:
        adminusername = request.form['adminusername']
        adminpassword = request.form['adminpassword']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM tbl_admin WHERE adminusername = % s AND adminpassword = % s', (adminusername, adminpassword, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['adminusername'] = account['adminusername']
            msg = 'Logged in successfully !'
            return redirect("/admindashboard")
        else:
            msg = '<h5 style="color:red">Incorrect username / password</h5>'
    return render_template('index.html', msg = msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('adminusername', None)
    return render_template('index.html')

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'firstname' in request.form and 'lastname' in request.form and 'age' in request.form and 'username' in request.form and 'password' in request.form:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM tbl_user WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not firstname or not lastname or not age or not username or not password:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO tbl_user VALUES (NULL, % s, % s, % s, %s, %s)', (firstname, lastname, age, username, password, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('index.html', msg = msg)


@app.route("/user-profile", methods = ["GET", "POST"])
def userprofile():
    if not session.get("username"):
        return redirect("/login")

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM tbl_user WHERE username = % s', (session['username'], ))
    data = cursor.fetchone()

    return render_template("user-profile.html", data = data)

@app.route("/adminprofile", methods = ["GET", "POST"])
def adminprofile():
    if not session.get("adminusername"):
        return redirect("/adminlogin")

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM tbl_admin WHERE adminusername = % s', (session['adminusername'], ))
    aprofile = cursor.fetchone()

    return render_template("admin-profile.html", aprofile = aprofile)

@app.route("/admindashboard", methods = ["GET", "POST"])
def admindashboard():
    if not session.get("adminusername"):    
        return redirect("/adminlogin")

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM tbl_user')
    users = cursor.fetchall()

    return render_template("admin-dashboard.html", users = users)

@app.route("/mental-health", methods = ["GET", "POST"])
def mentalhealth():
    if not session.get("username"):
        return redirect("/login")
    
    global p1, pr1, p2, pr2, p3, pr3, pr4
    if request.method == "POST":
        d1 = request.form['d1']
        d2 = request.form['d2']
        d3 = request.form['d3']
        d4 = request.form['d4']
        d5 = request.form['d5']
        d6 = request.form['d6']
        d7 = request.form['d7']
        a1 = request.form['a1']
        a2 = request.form['a2']
        a3 = request.form['a3']
        a4 = request.form['a4']
        a5 = request.form['a5']
        a6 = request.form['a6']
        a7 = request.form['a7']
        s1 = request.form['s1']
        s2 = request.form['s2']
        s3 = request.form['s3']
        s4 = request.form['s4']
        s5 = request.form['s5']
        s6 = request.form['s6']
        s7 = request.form['s7']
        
        p1 = prediction.depression_pred((d1, d2, d3, d4, d5, d6, d7))
        if p1 == 'Normal':
            pr1 = "Within Normal Limits"
        elif p1 == 'Mild':
            pr1 = "Mild"
        elif p1 == 'Moderate':
            pr1 = "Moderate"
        elif p1 == 'Severe':
            pr1 = "Severe"
        elif p1 == 'Extremely Severe':
            pr1 = "Extremely Severe"
        
        p3 = prediction.anxiety_pred((a1, a2, a3, a4, a5, a6, a7))
        if p3 == 'Normal':
            pr3 = "Within Normal Limits"
        elif p3 == 'Mild':
            pr3 = "Mild"
        elif p3 == 'Moderate':
            pr3 = "Moderate"
        elif p3 == 'Severe':
            pr3 = "Severe"
        elif p3 == 'Extremely Severe':
            pr3 = "Extremely Severe"

        p2 = prediction.stress_pred((s1, s2, s3, s4, s5, s6, s7))
        if p2 == 'Normal':
            pr2 = "Within Normal Limits"
        elif p2 == 'Mild':
            pr2 = "Mild"
        elif p2 == 'Moderate':
            pr2 = "Moderate"
        elif p2 == 'Severe':
            pr2 = "Severe"
        elif p2 == 'Extremely Severe':
            pr2 = "Extremely Severe"
            
        if (p1 == 'Severe' or p1 == 'Extremely Severe' or p2 =='Severe' or p2 == 'Extremely Severe' or p3 =='Severe' or p3 == 'Extremely Severe'):
            pr4 = "Your severity level is above the normal conditions. <br>You should consider to book the appointment immediately with the doctor."
        else:
            pr4 = ""
    return render_template("mental-health.html", pr1 = pr1, pr3 = pr3, pr2 = pr2, pr4 = pr4)

@app.route("/happy", methods = ["GET", "POST"])
def happy():
    if not session.get("username"):
        return redirect("/login")
    
    global p4, pr5
    if request.method == "POST":
        h1 = request.form['h1']
        h2 = request.form['h2']
        h3 = request.form['h3']
        h4 = request.form['h4']
        h5 = request.form['h5']
        h6 = request.form['h6']
        h7 = request.form['h7']
        h8 = request.form['h8']
        p4 = prediction.happy_pred((int(h1), int(h2), int(h3), int(h4), int(h5), int(h6), int(h7), int(h8)))
        
        if (p4 < 32):
            pr5 = "<h3 id = 'above-threshold'>Your happiness score is low. <br>You should consider to book the appointment with the doctor.</h3>"
        elif(p4 >= 32):
            pr5 = "<h3 id = 'below-threshold'>Your happiness score is good.</h3>"
        p4 = str(p4)
    return render_template("happy.html", p4 = p4, pr5 = pr5)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)