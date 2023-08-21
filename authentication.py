import os
import requests

api_address = 'authentication-test'
api_port = 8000

users = [
    {'username': 'alice', 'password': 'wonderland'},
    {'username': 'bob', 'password': 'builder'},
    {'username': 'clementine', 'password': 'mandarine'}
]

output_template = '''
============================
    Authentication test
============================
request done at "/permissions"
| username="{username}"
| password="{password}"
expected result = 200
actual result = {status_code}
==>  {test_status}
'''

for user in users:
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params=user
    )
    
    
    output = output_template.format(
        username=user['username'],
        password=user['password'],
        status_code=r.status_code,
        test_status='SUCCESS' if r.status_code == 200 else 'FAILURE'
    )
    
    if os.environ.get('LOG') == '1':
        with open('./logs/api_test.log', 'a') as file:
           file.write(output)

           