import requests
from pprint import pprint

r = requests.get('http://localhost:8123/list_streams')
topics_info = r.json()

pprint(topics_info)

for topic in topics_info["topics"]:
    print(topic)