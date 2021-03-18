from shared.database import db
from models.user import UserModel


class AnagramModel(db.Model):
    """
    Model used to store the word and his anagram.
        - Anagram column with index to speed up the search.
        - Only the owner of the word is able to delete it.
    """
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(), unique=True, nullable=False)
    anagram = db.Column(db.String(), nullable=False, index=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(UserModel.id), nullable=False)

    def to_json(self):
        return {'word': self.word, 'anagram': self.anagram}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return True

    def delete(self, user):
        if user.id == self.owner_id:
            db.session.delete(self)
            db.session.commit()
            return True
        else:
            return False

    def __init__(self, word, anagram, owner):
        self.word = word
        self.anagram = anagram
        self.owner_id = owner

    def __str__(self):
        return self.word
