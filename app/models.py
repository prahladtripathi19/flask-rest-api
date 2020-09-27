from app import app, db
import app.utils as utils
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Notes(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	note = db.Column(db.Text, nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
		'note': utils.decrypt(self.note)
		}