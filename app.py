from flask import Flask, request
from plate.generate import generate_num_car_license_plates
from plate.is_plate import is_plate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError
import bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import timedelta
from config import *
from passlib.hash import bcrypt


app = Flask(__name__)
app.config['SECRET_KEY']='test'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
jwt = JWTManager(app)

class License_plates(db.Model):
    __tablename__ = "license_plates"
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(6), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f'{self.id} {self.license_plate}'

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))

    def __init__(self, **kwargs) -> None:
        self.login = kwargs.get('login')
        self.password = bcrypt.hash(kwargs.get('password'))

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id, expires_delta=expire_delta
        )
        return token

    def __repr__(self) -> str:
        return f'{self.id} {self.login} {self.password}'

    @classmethod
    def authenticate(cls, login, password):
        user = cls.query.filter(cls.login == login).one()
        if not bcrypt.verify(password, user.password):
            raise Exception('No user with this password')
        return user
    

@app.route('/plate/generate/', methods=['GET'])
@jwt_required()
def get_generated_plates():
    amount = request.args.get('amount')

    try:
        amount = int(amount)
    except ValueError:
        req = {
            'message' : 'Invalid amount'
        }
    else:
        if amount > 0:
            req = generate_num_car_license_plates(amount)
        else:
            req = {
                'message' : 'Invalid amount'
            }
    finally:
        return req

@app.route('/plate/get/', methods=['GET'])
@jwt_required()
def get_plate_by_id():
    id = request.args.get('id')

    try:
        id = int(id)
        license_plate = License_plates.query.get_or_404(id).license_plate
    except ValueError:
        req = {
            'message' : 'Invalid id'
        }
    except NotFound:
        req = {
            'message' : 'Not found'
        }
    else:
        req = {
            'id' : id,
            'license_plate' : license_plate
        }
    finally:
        return req

@app.route('/plate/add/', methods=['POST'])
@jwt_required()
def add_plate_in_db():
    plate = request.json.values()

    if is_plate(plate):
        try:
            db.session.add(License_plates(license_plate=plate))
            req = { 
                'license_plate' : plate
            }
            db.session.commit()
        except IntegrityError:
            req = {
                'message' : 'Already exist'
        }
    else:
        req = {
            'message' : 'Invalid plate'
        }
    return req
    
@app.route('/plate/register', methods=['POST'])
def register():
    params = request.json
    user = Users(**params)
    db.session.add(user)
    db.session.commit()
    token = user.get_token()
    return {'acces_token': token}

@app.route('/plate/login', methods=['POST'])
def login():
    params = request.json
    user = Users.authenticate(**params)
    token = user.get_token()
    return {'acces_token': token}


if __name__ == '__main__':
    app.run(host=host)