import requests, json


def shuffle_teams(teams):
    raw_data = {
        "jsonrpc": "2.0",
        "method": "generateIntegerSequences",
        "params": {
            "apiKey": "d6eefee9-1e35-4324-b3c3-02f70e966cf2",
            "n": 1,
            "length": [len(teams)],
            "min": [1],
            "max": [len(teams)],
            "replacement": [False],
            "base": [10]
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

    # parse json response
    response_json = response.json()

    # extract result
    result = response_json['result']['random']['data'][0]
    print(result)
    return result
