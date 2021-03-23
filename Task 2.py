import requests

session = requests.Session()

alphabet = dict()


def add_to_alphabet(animal: str, dictionary: dict):
    if animal[0] not in dictionary:
        dictionary[animal[0]] = 1
    else:
        dictionary[animal[0]] += 1


url = "https://ru.wikipedia.org/w/api.php"

params = {
    'action': 'query',
    'format': 'json',
    'list': 'categorymembers',
    'cmtitle': 'Категория:Животные по алфавиту',
    'cmlimit': 500
}

while True:
    try:
        response = session.get(url, params=params)
        data = response.json()
        for anim in data['query']['categorymembers']:
            add_to_alphabet(anim['title'], alphabet)
        if 'continue' in data and 'cmcontinue' in data['continue']:
            params['cmcontinue'] = data['continue']['cmcontinue']
        else:
            break
    except requests.exceptions.ConnectionError:
        print('problems')
        continue

[print(f'{k}{alphabet[k]}') for k in sorted(alphabet)]
