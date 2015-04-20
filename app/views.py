# views are handlers that respond to requests from web browsers or other clients
# Each view function maps to one or more request URLs
from flask import render_template, flash, redirect
from app import app
from .forms import Deck

#./run.py

@app.route('/submit', methods=('GET', 'POST'))
def submit():
	form = Deck()
	if form.validate_on_submit():
		return redirect('/index')
	return render_template('submit.html',
							title='Create Card',
							form=form)

@app.route('/')
@app.route('/index')
def index():
	# This is displayed on client's web browser
	user = {'nickname': 'Enrique Iglesias'}		#fake user
	decks = [
	{
		'title': 'GRE Words',
		'cards': [
			{
				'word': 'combust',
				'definition': 'to catch on fire'
			},
			{
				'word': 'phaze',
				'definition': 'to be affected'
			}
		]
	},
	{
		'title': 'Food words',
		'cards': [
			{
				'word': 'amuse bouche',
				'definition': 'little serving'
			},
			{
				'word': 'kimchii',
				'definition': 'femented cabbage'
			}
		]
	}
	]
	return render_template('index.html',
							title ='Home',
							user=user,
							posts=decks)
