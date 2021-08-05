from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

class Data(db.Model):
    # table containing key, value pairs

    __tablename__ = 'data'

    data_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    key = db.Column(db.String, nullable=False, unique=True)
    value = db.Column(db.String, nullable=False)

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        # human readable representation of key,value pair

        return f"""<Data data_id={self.data_id} key={self.key} value={self.value}>"""

def connect_to_db(app):
    # connects db to Flask app

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///correlated"
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.create_all()
    db.init_app(app)

if __name__ == '__main__':
    # from server import app
    connect_to_db(app)