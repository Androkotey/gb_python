import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'NDFkZjVkZTYtYzdhOC00M2VhLWFmMzQtMTBmZjlhNWEwOTM5OjJkNDgyMjM3YjQ3ZDRkMzhiNzEyZDZkZDFlMmNlYWVl'

headers_auth = {"Authorization": "Basic " + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    token = auth.text

    with open('4.txt', 'r', encoding='utf-8') as source_file:
        with open('4_out.txt', 'w', encoding='utf-8') as output_file:
            for line in source_file:
                word_to_translate = line.split()[0].lower()  # забавный перевод для One и Two (с заглавной буквы)
                headers_translate = {'Authorization': 'Bearer ' + token}
                params = {'text': word_to_translate,
                          'srcLang': 1033,
                          'dstLang': 1049}
                r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)

                res = r.json()
                try:
                    print(' '.join([res["Translation"]["Translation"].title()] + line.split()[1:]), file=output_file)
                except TypeError:
                    print('Error!')
else:
    print('Error!')
