from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="SecretKeyMePls"
@app.route('/')
def index():
	return render_template("index.html")
@app.route('/result', methods=['POST'])
def result():
	if request.method == 'POST':
		session['name'] = request.form['name']
		session['location'] = request.form['location']
		session['language'] = request.form['language']
		session['comment'] = request.form['comment']
		if len(session['name']) < 1 and len(session['comment']) < 1:
			flash("Name cannot be empty!")
			flash("Just kidding! Comment cannot be empty!")
			return redirect('/')
		elif len(session['name']) < 1:
			flash("Name cannot be empty!")
			return redirect('/')
		elif len(session['comment']) < 1:
			flash("Just kidding! Comment cannot be empty!")
			return redirect('/')
		elif len(session['comment']) > 120:
			flash("Your comment is limited to 120 characters!")
			return redirect('/')
		else:
			return render_template("result.html")
app.run(debug=True)