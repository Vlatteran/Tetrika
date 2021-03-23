import requests

S = requests.Session()

alphabet = dict()


def add_to_alphabet(animal: str, dictionary: dict):
    if animal[0] not in dictionary:
        dictionary[animal[0]] = 1
    else:
        dictionary[animal[0]] += 1


URL = "https://ru.wikipedia.org/w/api.php"

PARAMS = {
    'action': 'query',
    'format': 'json',
    'list': 'categorymembers',
    'cmtitle': 'Категория:Животные по алфавиту',
    'cmlimit': 500
}

while True:
    try:
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        for anim in DATA['query']['categorymembers']:
            add_to_alphabet(anim['title'], alphabet)
        if 'continue' in DATA and 'cmcontinue' in DATA['continue']:
            PARAMS['cmcontinue'] = DATA['continue']['cmcontinue']
        else:
            break
    except requests.exceptions.ConnectionError:
        print('problems')
        continue

[print(f'{k}{alphabet[k]}') for k in sorted(alphabet)]
