from flask_restful import Resource, http_status_message
from models.anagram import AnagramModel
import json


class Anagram(Resource):

    def get(self, word):
        if word:
            anagram = ''.join(sorted(word))
            words = AnagramModel.query.filter_by(anagram=anagram).all()
            result = [word.to_json() for word in words]
            http_code = 200
        else:
            result = []
            http_code = 400

        return json.dumps(result, indent=4, separators=(',', ': ')), http_code

    def put(self, word):
        if word:
            result = AnagramModel.query.filter_by(word=word).first()  # Taking only first, as are unique values

            if not result:
                anagram = ''.join(sorted(word))
                new_entry = AnagramModel(word=word, anagram=anagram)
                new_entry.create()
                http_code = 201
            else:
                http_code = 200
        else:
            http_code = 400

        return http_status_message(http_code), http_code

    def delete(self, word):
        if word:
            result = AnagramModel.query.filter_by(word=word).first()  # Taking only first, as are unique values

            if result:
                result.delete()
                http_code = 202
            else:
                http_code = 404
        else:
            http_code = 400

        return http_status_message(http_code), http_code
