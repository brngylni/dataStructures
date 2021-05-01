import requests
import json

result = requests.get("http://ensonhaber.com")
result = result.text


print(result)
print(type(result))
