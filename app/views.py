from flask import request,jsonify
from flask_restful import Resource, Api
from app import app, db
from flask_bcrypt import Bcrypt
from app.models import User, Notes
import app.utils as utils
api = Api(app)
bcrypt = Bcrypt(app)

class UserRegistration(Resource):
    def post(self):
    	context = request.get_json()
    	username = context['username']
    	password = context['password']
    	if username and password:
    		user = User.query.filter_by(username=username).first()
    		if user is None:
    			password = bcrypt.generate_password_hash(password)
    			user = User(username=username, password=password)
    			db.session.add(user)
    			db.session.commit()
    			return {"status":"account created"}
    		else:
    			return {"status":"User already exist."}
    	else:
    		return {"status":"The username and password can not be blank"}

class Authlogin(Resource):
    def post(self):
    	context = request.get_json()
    	username = context['username']
    	password = context['password']
    	if username and password:
    		user = User.query.filter_by(username=username).first()
    		if user is not None:
    			if bcrypt.check_password_hash(user.password, password):
    				return {"status":"success","userId":user.id}
    			else:
    				return {"status":"Username or password is incorrect"}
    		else:
    			return {"status":"User not exist."}
    	else:
    		return {"status":"The username and password can not be blank"}

class getSiteList(Resource):
    def get(self):
    	user_id = request.args.get('user')
    	if user_id:
    		user = User.query.filter_by(id=user_id).first()
    		if user is not None:
    			notes = Notes.query.filter_by(user_id=user_id)
    			return [i.serialize for i in notes]
    		else:
    			return {"status":"You are not Authorize to access it."}
    	else:
    		return {"status":"You are not Authorize to access it"}

class SaveSiteList(Resource):
    def post(self):
    	context = request.get_json()
    	user_id = request.args.get('user')
    	note = context['note']
    	if user_id:
    		user = User.query.filter_by(id=user_id).first()
    		if user is not None:
    			notesobj = Notes(note= (utils.encrypt(note)), user_id=user_id)
    			db.session.add(notesobj)
    			db.session.commit()
    			return {"status":"success"}
    		else:
    			return {"status":"User not exist."}
    	else:
    		return {"status":"The username and password can not be blank"}


api.add_resource(UserRegistration, '/app/user')
api.add_resource(Authlogin, '/app/user/auth')
api.add_resource(getSiteList, '/app/sites/list')
api.add_resource(SaveSiteList, '/app/sites')