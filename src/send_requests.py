import requests


#url = 'http://0.0.0.0:5050/get-recomm/'
url = 'https://recomm-microservice.herokuapp.com/'

params = {'act1': 'Focus excercise', 'act2': 'Sleeping excercise', 'act3': 'Flexibility excercise'}

r = requests.post(url, params=params)

print(r.text)
