import requests
import csv

def fetch_and_print_posts():
    recuperar = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {recuperar.status_code}')

    if recuperar.status_code == 200:
        publicaciones = recuperar.json()
        for i in publicaciones:
            print(i['title'])

def fetch_and_save_posts():
    list_dic = []
    recuperar = requests.get('https://jsonplaceholder.typicode.com/posts')
    if recuperar.status_code == 200:
        publicacion = recuperar.json()
        for post in publicacion:
            list_dic.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

    with open('posts.csv', 'w', newline='') as f:
        write = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
        write.writeheader()
        write.writerows(list_dic)
