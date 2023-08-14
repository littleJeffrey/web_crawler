from flask import Flask, request, abort, render_template
from flask import send_from_directory

import flask_sqlalchemy
import flask_restless

from flask_cors import CORS
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///static/data/nobel_winners.db'
app.config['CORS_ALLOW_HEADERS']="Content-Type"
app.config['CORS_RESOURCES']={r"/api/*":{"origins":"*"}}

cors=CORS(app)

db = flask_sqlalchemy.SQLAlchemy(app)

class Winners(db.Model):
    __tablename__ = 'winners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    category = db.Column(db.Unicode)
    year = db.Column(db.Unicode)
    nationality = db.Column(db.Unicode)
    gender = db.Column(db.Unicode)

db.create_all()
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Winners, methods=['GET','POST','DELETE'],max_results_per_page=1000)
@app.route('/',methods=['GET'])
def root():
    return send_from_directory('.','templates/index.html')
if __name__=='__main__':
    app.run(port=9000)