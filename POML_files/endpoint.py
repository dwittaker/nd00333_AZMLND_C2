import requests
import json

# URL for the web service, should be similar to:
# 
scoring_uri = 'http://655d6fd5-7a37-4b09-ab6c-8581f9bd0068.southcentralus.azurecontainer.io/score'

# If the service is authenticated, set the key or token
key = "f26Zq8heP3zJfC9aFU820YmaK4oehrqL"

# Two sets of data to score, so we get two results back
data = {
    "data":
    [
        {
            'age': "24",
            'job': "entrepreneur",
            'marital': "married",
            'education': "university.degree",
            'default': "no",
            'housing': "yes",
            'loan': "yes",
            'contact': "telephone",
            'month': "jun",
            'day_of_week': "wed",
            'duration': "126",
            'campaign': "4",
            'pdays': "999",
            'previous': "0",
            'poutcome': "nonexistent",
            'emp.var.rate': "1.4",
            'cons.price.idx': "94.465",
            'cons.conf.idx': "-41.8",
            'euribor3m': "4.962",
            'nr.employed': "5228.1",
        }
    ,
        {
            'age': "80",
            'job': "retired",
            'marital': "married",
            'education': "high.school",
            'default': "yes",
            'housing': "yes",
            'loan': "yes",
            'contact': "telephone",
            'month': "jun",
            'day_of_week': "wed",
            'duration': "1136",
            'campaign': "4",
            'pdays': "999",
            'previous': "0",
            'poutcome': "nonexistent",
            'emp.var.rate': "1.4",
            'cons.price.idx': "93.465",
            'cons.conf.idx': "-43.8",
            'euribor3m': "4.962",
            'nr.employed': "5228.1",
        }
    ]
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
