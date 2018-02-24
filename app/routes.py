from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {"username" : "Bob"}
	posts = [
		{
			'author' : {'username':'John'},
			'body' : 'Beautiful day in London!'
		},
		{
			'author' : {'username':'Sarah'},
			'body' : "I love the sunshine!"
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
