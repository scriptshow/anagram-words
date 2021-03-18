from flask_restful import Resource, http_status_message
from models.anagram import AnagramModel
from shared.authentication import auth


class Anagram(Resource):
    """
    Anagram resource, will manage all the API operations with words related.
    """
    def __init__(self, **kwargs):
        self.secret_key = kwargs['secret_key']

    def get(self, word=None):
        """
        Function to list all the words that matches with the anagram of word given, this function will be
        allowed for not authenticated users.

        :param word: word to search all the anagrams related.
        :return: list of words with related anagrams.
        """
        if word:
            anagram = ''.join(sorted(word))
            words = AnagramModel.query.filter_by(anagram=anagram).all()
            result = [word.to_json() for word in words]
            http_code = 200
        else:
            result = []
            http_code = 400

        return result, http_code

    @auth.login_required
    def put(self, word):
        """
        Function to add a new word to the database, where all words are stored. Only authenticated users can
        add new words.

        :param word: word to be added.
        :return: set of word-anagram that has been added, or an message.
        """
        user = auth.current_user()
        if word:
            result = AnagramModel.query.filter_by(word=word).first()  # Taking only first, as are unique values

            if not result:
                anagram = ''.join(sorted(word))
                new_entry = AnagramModel(word=word, anagram=anagram, owner=user.id)
                new_entry.create()
                response = new_entry.to_json()
                http_code = 201
            else:
                http_code = 200
                response = "Already exists"
        else:
            http_code = 400
            response = http_status_message(http_code)

        return response, http_code

    @auth.login_required
    def delete(self, word):
        """
        Function to delete an existing word from the database. Only authenticated users can delete words,
        and only the words where the user is owner can be deleted.

        :param word: word to be deleted.
        :return: string message about the operation result.
        """
        user = auth.current_user()
        if word:
            result = AnagramModel.query.filter_by(word=word).first()  # Taking only first, as are unique values

            if result:
                if result.delete(user):
                    http_code = 200
                else:
                    http_code = 401
            else:
                http_code = 404
        else:
            http_code = 400

        return http_status_message(http_code), http_code
