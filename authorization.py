import os
import requests

api_address = 'authorization-test'
api_port = 8000

users = [
    {'username': 'alice', 'password': 'wonderland'},
    {'username': 'bob', 'password': 'builder'}
]

sentences = [
    "you got this",
]

output_template = '''
============================
    Authorization test
============================

| username="{username}"
| password="{password}"
| sentence="{sentence}"
| version="{version}"
expected result = 200
actual result = {status_code}
==>  {test_status}
'''

for user in users:
    for sentence in sentences:
        for version in ['v1', 'v2']:
            payload = {
                'username': user['username'],
                'password': user['password'],
                'sentence': sentence
            }
            
            url = 'http://{address}:{port}/{version}/sentiment'.format(
                address=api_address, port=api_port, version=version
            )
            
            r = requests.get(url, params=payload)
            
            if r.status_code == 200:
                test_status = 'SUCCESS'
            elif r.status_code == 403:
                test_status = 'FAILURE'
            else:
                test_status = f'UNKNOWN STATUS CODE: {r.status_code}'
            
            output = output_template.format(
                username=user['username'],
                password=user['password'],
                sentence=sentence,
                version=version,
                status_code=r.status_code,
                test_status=test_status
            )
            
            
            if os.environ.get('LOG') == '1':
                with open('./logs/api_test.log', 'a') as file:
                    file.write(output)