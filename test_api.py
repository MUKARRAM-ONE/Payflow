import requests

session = requests.Session()
login_data = {'username': 'mukarram', 'password': 'admin123'}
r = session.post('http://127.0.0.1:5000/auth/login', data=login_data)
print("Login status:", r.status_code)

r = session.get('http://127.0.0.1:5000/master/get/location')
print("Locations:", r.json())

r = session.get('http://127.0.0.1:5000/master/get/city')
print("Cities:", r.json())
