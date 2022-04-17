import json
import requests
import time

response_API = requests.get('https://catfact.ninja/fact')
print(response_API)
facts = response_API.text
print(facts)

