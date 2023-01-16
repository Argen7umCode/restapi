import requests


res = requests.get('http://127.0.0.1:3000/api/plate/generate/100000')
print(res.json())


res = requests.get('http://127.0.0.1:3000/api/plate/generate/0')
print(res.json())