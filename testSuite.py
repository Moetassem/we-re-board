from app import app, db
import unittest
import json


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ozqhfdunsqxrnj:758183f57a6468bbfd5f6f4f99c6a753f1e3a2afae37699c8922ca520a488bd3@ec2-52-203-98-126.compute-1.amazonaws.com:5432/d674iu1eqcu3l9"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app = app.test_client()

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        #response = tester.get('/login', content_type='html/text')
        #self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        #response = tester.get('/login')
        #self.assertIn(b'Please login', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        tester = app.test_client()
        # #response = tester.post('/login',
        #                        data=dict(username="admin", password="admin"),
        #                        follow_redirects=True
        #                        )
        #self.assertIn(b'You were logged in', response.data)

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client()
        # #response = tester.post('/login',
        #                        data=dict(username="wrong", password="wrong"),
        #                        follow_redirects=True
        #                        )
        #self.assertIn(b'Invalid Credentials. Please try again.', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        tester = app.test_client()
        # #tester.post('/login',
        #             data=dict(username="admin", password="admin"),
        #             follow_redirects=True
        #             )
        # response = tester.get('/logout', follow_redirects=True)
        # self.assertIn(b'You were logged out', response.data)

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        tester = app.test_client()
        # response = tester.get('/', follow_redirects=True)
        # self.assertIn(b'You need to login first.', response.data)

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
         tester = app.test_client()
        # response = tester.get('/logout', follow_redirects=True)
        # self.assertIn(b'You need to login first.', response.data)

    # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):
        tester = app.test_client()
        # response = tester.post('/login',
        #                        data=dict(username="admin", password="admin"),
        #                        follow_redirects=True
        #                        )
        # self.assertIn(b'Hello from the shell', response.data)

    def test_create_user(self, name, email, password):
        
        data = {
            'name': name,
            'email': email,
            'password': password
        }

        return self.app.post(
            '/user',
            data=json.dumps(data),
            follow_redirects=True
        )

    def test_create_user_working(self):
        response = self.test_create_user("testUser", "testUser@gmail.com", "1234qwer")
        self.assertEqual(response.status_code, 200)

    #def test_create_user_fail(self):
     #   response = self.test_create_user("testUser2", "testUser2@gmail.com", "testUseremail")
      #  self.assertEqual(response.status_code, 500)

    def test_create_user_duplicate_mail(self):
        response = self.test_create_user("John Doe", "johndoe@gmail.com", "p4ssw0rd")
        self.assertEqual(response.status_code, 200)
        response = self.test_create_user("John Doe", "johndoe@gmail.com", "pAsSwOrD")
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
