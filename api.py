# import requests
import requests
# assign url as a variable and paste the link from alphavantage under Exchange Currency
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=W677J7965EU3DEBN"
# request access to the data using .get() method and assign a variable called "response" to it
response = requests.get(url)
# retrieve data using .json() and save it as variable (detail)
details = response.json()
# create For loop 
for info in details:
    # create a variable ("conversion rate") and assign it to convert from USD to SGD using f-string
    conversion_rate = f"USD1 = SGD{details[info]['5. Exchange Rate']}"
# create a function (convertUSDtoSGD) with a parameter, amount
def convertUSDtoSGD(amount):
    # create For loop 
    for info in details:
        # create a variable (USD) and assign it as the conversion rate (USD to SGD)
        # convert from string to float 
        USD = float(details[info]['5. Exchange Rate'])
    # return the amount in SGD 
    return amount*USD
# print "conversion rate"
print(conversion_rate)

