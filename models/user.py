from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from shared.encryption import encrypt, verify
from shared.database import db
from shared.authentication import auth
from shared.config import SECRET_KEY


class UserModel(db.Model):
    """
    User model, used to register and authenticate the users
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return True

    def update_password(self, password):
        self.hash_password(password)
        db.session.commit()
        return True

    def hash_password(self, password):
        self.password_hash = encrypt(password.encode('utf-8'))
        return self.password_hash

    def verify_password(self, password):
        return verify(password.encode('utf-8'), self.password_hash)

    def generate_auth_token(self, secret_key=None, expiration=600):
        if secret_key:
            s = Serializer(secret_key, expires_in=expiration)
            return s.dumps({'id': self.id}).decode("utf-8")
        else:
            return None

    @staticmethod
    @auth.verify_token
    def verify_auth_token(token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = UserModel.query.get(data['id'])
        return user

    def __init__(self, username, password):
        self.username = username
        self.hash_password(password)
