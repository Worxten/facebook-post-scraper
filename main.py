from scraper import extract
import json

if __name__ == '__main__':
    list = extract("https://www.facebook.com/mercadolibrecol", 200, False, True)
    for post in list:
        print(post)

    with open('output.json', 'w',encoding='utf8') as file:
        file.write('[')
        for post in list:
            file.write(json.dumps(post, ensure_ascii=False))
            file.write(',')
        file.write(']')

