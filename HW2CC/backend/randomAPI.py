import requests, json

raw_data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": "d6eefee9-1e35-4324-b3c3-02f70e966cf2",
        "n": 3,
        "min": 1,
        "max": 100,
        "replacement": True
    },
    'id': 1
}

headers = {'Content-type': 'application/json', 'Content-Length': '200', 'Accept': 'application/json'}

data = json.dumps(raw_data)

response = requests.post(
    url='https://api.random.org/json-rpc/2/invoke',
    data=data,
    headers=headers
)

#parse json response
response_json = response.json()

#extract result
result = response_json['result']['random']['data']

print(result)