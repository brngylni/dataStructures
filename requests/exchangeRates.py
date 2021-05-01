import requests
import json


base = input("Please enter the money unit that you want to exchange : ")

result = requests.get('https://api.exchangeratesapi.io/latest?base='+base)
result = json.loads(result.text)

print("Here is the exchange rates : ")

for i in result["rates"]:
    print(i, " : ", result["rates"][i])

desiredUnit = input("Please enter the unit that you want to exchange with : ")
amount = float(input("Please enter the amount : "))
process = amount * result["rates"][desiredUnit]

print("Congratulation! You've ", process, desiredUnit, " now.")

