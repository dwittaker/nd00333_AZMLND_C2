import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
data = {
    "data":
    [
        {
            'age': "0",
            'job': "example_value",
            'marital': "example_value",
            'education': "example_value",
            'default': "example_value",
            'housing': "example_value",
            'loan': "example_value",
            'contact': "example_value",
            'month': "example_value",
            'day_of_week': "example_value",
            'duration': "0",
            'campaign': "0",
            'pdays': "0",
            'previous': "0",
            'poutcome': "example_value",
            'emp.var.rate': "0",
            'cons.price.idx': "0",
            'cons.conf.idx': "0",
            'euribor3m': "0",
            'nr.employed': "0",
        },
    ],
}

body = str.encode(json.dumps(data))

url = 'http://655d6fd5-7a37-4b09-ab6c-8581f9bd0068.southcentralus.azurecontainer.io/score'
api_key = 'f26Zq8heP3zJfC9aFU820YmaK4oehrqL' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))