import flask
import mysql.connector

 
app = flask.Flask(__name__)
cnx = mysql.connector.connect(user='root', password='JpNorena97', host='localhost', database='finaltel',auth_plugin='mysql_native_password')


@app.route('/')
def home():
        return flask.render_template('index.html')


@app.route('/profile')	
def profile():
		return flask.render_template('profile.html')	

@app.route('/login', methods =['GET', 'POST'])
def login():
	cursor = cnx.cursor()
	if flask.request.method == 'POST' and 'username' in flask.request.form and 'password' in flask.request.form:
		
		username = flask.request.form['username']
		password = flask.request.form['password']
		consulta = ("SELECT Nombre , Contraseña FROM users WHERE Nombre = %s AND Contraseña = %s")
		nombre = username
		contra = password
		cursor.execute(consulta, (nombre, contra))
		for (Nombre, Contraseña) in cursor:
			print("{} , {} ".format(Nombre,Contraseña))
		cursor.close()

	return flask.render_template('login.html')

	
@app.route('/register', methods =['GET', 'POST'])
def register():
	cursor = cnx.cursor()
	if flask.request.method == 'POST' and 'username' in flask.request.form and 'password' in flask.request.form  :
		username = flask.request.form['username']
		password = flask.request.form['password']
		add_user = ("INSERT INTO users"
		"(Nombre, Contraseña)"
		"VALUES (%s,%s)")
		data_user = (username,password)
		cursor.execute(add_user,data_user)
		cnx.commit()
		cursor.close()
			
	return flask.render_template('register.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=80)
