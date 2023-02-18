import requests

response = requests.get('https://api.github.com/events')
events = response.json()

for event in events:
    type = event['type']
    actor_login=event["actor"] ["login"]
    repo_name = event['repo']['name']
    url = event['repo']['url']

    print(f'Repo name: {repo_name}')
    print(f'actor login: {actor_login}')
    print(f'type: {type}')
    print(f'URL: {url}')
    print('m -' * 100)