# create a function, 'convertUSDtoSGD' 
def convertUSDtoSGD():
    # give a description of the function using docstring
    """
    The program extracts from alphavantage.co and returns 
    the real time currency conversion rate. 
    No parameter is required.
    """
    #import built-in function, 'requests'
    import requests
    #create variable, 'url' to locate Exchange Currency from alphavantage.co
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=W677J7965EU3DEBN"
    #create variable, 'response' to request using requests keyword and access the data using .get() method
    response = requests.get(url)
    #create variable, 'details' to retrieve data using .json()
    details = response.json()
    #create For loop 
    for info in details:
        #create variable, 'USD' and assign it as the conversion rate (USD to SGD)
        #convert from string to float using float() function
        USD = float(details[info]['5. Exchange Rate'])
    #return USD using return keyword
    return USD
