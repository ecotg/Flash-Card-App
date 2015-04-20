# translate db schema into code
from werkzeug import generate_password_hash, check_password_hash
from app import db

class Definition(db.Model):
	__tablename__ = 'definition'
	word_id = db.Column(db.Integer, db.ForeignKey('cards.id'), index=True)
	definition = db.Column(db.String(128))
	id = db.Column(db.Integer,primary_key=True)

	def __repr__(self):
		return '<Definition %r with id: %r>' % (self.definition, self.id)


class Card(db.Model):
	__tablename__ = 'cards'
	word = db.Column(db.String(64),index=True)
	deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'))
	id = db.Column(db.Integer, primary_key=True)
	definitions = db.relationship('Definition', backref='cards',
									lazy='dynamic')

	def __repr__(self):
		return '<Card %r with id: %r>' % (self.word, self.id)


class Deck(db.Model):
	# Need a way to grab the user_id based on who's logged in
	__tablename__ ='decks' # not really needed
	deckTitle = db.Column(db.String(64), index=True, unique=True)
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	cards = db.relationship('Card',backref='decks',
								lazy='dynamic')

	def __repr__(self):
		return '<Deck %r with id: %r>' % (self.deckTitle, self.id)


class User(db.Model):
	__tablename__ ='users'
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	pwdhash = db.Column(db.String(54))
	# Creates a colunn called decks in the User table
	# 'Deck' signifies the many,
	# backref means that a field called users will be added to the Deck table
	#'users' points tback to the users objects
	# thus we can use deck.users to get the user of that deck
	decks = db.relationship('Deck', backref='users',
							lazy='dynamic' )

	def __init__(self,nickname, password):
		self.nickname = nickname.lower() #or title() to make titlecase
		self.set_password(password)

	def set_password(self,password):
		self.pwdhash = generate_password_hash(password)

	def check_password(self,password):
		return check_password_hash(self.pwdhash,password)

	def __repr__(self):
		return '<User %r with id %r >' % (self.nickname, self.id)
