from mongoengine import Document, StringField, connect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

connect('veterinaria', host='mongodb://localhost:27017/')

class Users(UserMixin, Document):
    username = StringField(required=True, unique=True)
    password_hash = StringField(required=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

users_query = Users.objects

if users_query.count() == 0:
    user = Users(username="admin", password_hash=generate_password_hash("admin"))
    user.save()