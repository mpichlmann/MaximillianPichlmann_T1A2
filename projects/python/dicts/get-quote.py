import requests 

res = requests.get('https://api.quotable.io/quotes/random')
quotes = res.json()[0]
print(quotes['content'])
print(f"--{quotes['author']}")
