import json
import requests


url = 'http://127.0.0.1:5001/hello'

headers = {
    'Content-Type': 'application/json'
}
body = {
    'message': 'nuga'
}

response = requests.post(
    url,
    headers=headers,
    data=json.dumps(body)
)

print(response.content)

