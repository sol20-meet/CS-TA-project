from database import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session
from model import *
from textblob import TextBlob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/index.html')
def home():
	a=query_all()
	return render_template('index.html', places=a)

@app.route('/')
def NewHome():
	return home()


@app.route('/about.html')
def About():
	return render_template('about.html')


@app.route('/upload.html' , methods=['GET','POST'])
def upload():
	if request.method == 'GET' :
		return render_template('upload.html')
	else:
		print("creating Place object")
		name_of_place = request.form['nameOfplace']
		description = request.form['subject']
		user = request.form['user']
		link = request.form['Link']
		#add_place is a function that creates a new object of a place based on the data that the user has entered in the webstie, and then it sends it to the database as a Place object.
		if len(user) == 0:
			user = "Anonymous User"
		if len(link) == 0:
			link = "https://wallpapercave.com/wp/wp4813075.jpg"

		add_place(name_of_place , description , user , link)
		return redirect('list.html')


@app.route('/list.html')
def fullList():
	places=query_all()
	return render_template('list.html',places=places)

@app.route('/place.html/<int:p_id>')
def place(p_id):
	place=session.query(Place).filter_by(id=p_id).one()
	if TextBlob(place.description).polarity > 0:
		polarity = "Positive!"
	else : 
		polarity = "Negative"
	return render_template('place.html',place=place , polarity = polarity)



if __name__ == '__main__':
	app.run(debug=True)
