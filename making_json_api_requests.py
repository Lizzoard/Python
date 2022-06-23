import requests

req = requests.get("https://swapi.dev/api/people/1/")
person = req.json()
print(f"Name is\t\t\t{person['name']}")
print(f"Birth year is\t\t{person['birth_year']}")

for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print("Film is: ",film['title'], film['release_date'])

for starship in person['starships']:
    req = requests.get(starship)
    starship = req.json()
    print("Starship " ,starship['name'])