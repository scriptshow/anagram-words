from shared.database import db


class AnagramModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(), unique=True, nullable=False)
    anagram = db.Column(db.String(), nullable=False)

    def to_json(self):
        return {'word': self.word, 'anagram': self.anagram}

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, word, anagram):
        self.word = word
        self.anagram = anagram

    def __str__(self):
        return self.word
