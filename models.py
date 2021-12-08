from werkzeug.security import generate_password_hash, check_password_hash

# ...

# ...
from flask_login import UserMixin

class User(UserMixin, db.Model):
    # ...

class User(db.Model):
    # ...

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

from app import login
# ...

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

from hashlib import md5
# ...

class User(UserMixin, db.Model):
    # ...
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
