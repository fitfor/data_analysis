import requests


#url = 'http://127.0.0.1:5000/get-recomm/'
url = 'https://recomm-microservice.herokuapp.com/get-recomm/'

params = {'act1': 'Focus excercise', 'act2': 'Sleeping excercise', 'act3': 'Flexibility excercise'}
#params = {'act1': 'HealthyEating', 'act2': 'Endurance excercise', 'act3': 'Motivation excercise'}

r = requests.post(url, params=params)

print(r.text)
