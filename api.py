#import the built-in module, 'requests'
import requests
#create a function, convertUSDtoSGD(), with no parameter
def convertUSDtoSGD():
    # give a description of the function using docstring
    """
    The program extracts information on the currency exchange rate from USD to SGD from alphavantage.co 
    and returns the value of SGD for each dollar of USD.
    No parameter is required.
    """
    #copy and paste the link from alphavantage.co and change the API parameters to CURRENCY_EXCHANGE_RATE for function, USD for from_currency and SGD for to_currency
    #assign the link to a variable, url
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=W677J7965EU3DEBN"
    #use the requests.get() method to read the existing resource that the url leads to
    #assign this object to a variable, response
    response = requests.get(url)
    #use the method .json() to retrieve data from the variable, response
    #assign the data, which is a dictionary, to another variable, details
    details = response.json()
    #create a for loop to retrieve the data from the variable, details
    for info in details:
        #use indexing to reference the conversion rate of USD to SGD
        #convert the value from a string to a float using the float() function
        USD = float(details[info]['5. Exchange Rate'])
    #return USD using return keyword
    return USD
