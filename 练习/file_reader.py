import json

filenamae = 'uaername.json'
with open(filenamae) as f:
    username = json.load(f)
    print(f"welcome back, {username}!")