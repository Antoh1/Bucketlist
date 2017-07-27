from app import app
import unittest

class bucketlistTestCases(unittest.TestCase):
	"""Testcases for the bucketlist functionalities"""
	
	#Ensure flask was setup correctly
	def test_home(self):
		tester = app.test_client(self)
		response = tester.get('/signin', content_type="html/text")
		self.assertEqual(response.status_code, 200)
    
    #Ensure the signin page loads correctly
	def test_signin_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/signin', content_type="html/text")
		self.assertTrue(b'Log in Here' in response.data)

	#Ensure that the signin page behaves correctly given correct credentials
	def test_correct_signin(self):
		tester = app.test_client(self)
		response = tester.post(
			'/signin',
			data = dict(email='admin@gmail.com', password='admin'),
			follow_redirects=True
		)
		self.assertTrue(b'View Bucketlist Items' in response.data)
	
	#Ensure that the signin page behaves correctly given incorrect credentials
	def test_incorrect_signin(self):
		tester = app.test_client(self)
		response = tester.post(
			'/signin',
			data = dict(email='wrong', password='wrong'),
			follow_redirects=True
		)
		self.assertTrue(b'Wrong Signin Credentials, Kindly confirm and signin again' in response.data)

	#Ensure logout behaves correctly



if __name__ == '__main__':
    unittest.main()		
