import unittest
from app import app, db
import json


class UserTestCase(unittest.TestCase):
    """
    Tests cases for the Users.
    """

    def setUp(self):
        """
        Initializing values to be used in the test cases.
        """
        self.app = app
        self.client = self.app.test_client
        self.username = 'test'
        self.password = 'testpw'
        self.token = None

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_user_creation(self):
        """
        Test API can create a user (POST request).
        """
        res = self.client().post('/signup', data={'username': self.username, 'password': self.password})
        self.assertEqual(res.status_code, 201)
        self.assertIn('token', str(res.data.decode('utf-8')))

    def test_user_login(self):
        """
        Test user can logged in (POST request).
        """
        self.test_user_creation()
        res = self.client().post('/login', data={'username': self.username, 'password': self.password})
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.token = data['token']
        self.assertIn('token', str(res.data.decode('utf-8')))

    def tearDown(self):
        """
        Teardown all initialized variables.
        """
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
