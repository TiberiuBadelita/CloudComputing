from flask import Flask, request
from flask_cors import CORS
import requests, json, competitionHandler

import randomAPI, smsAPI

my_api_url = "http://localhost:8081/"
app = Flask("Football App")
CORS(app)


@app.route('/')
def index():
    return "Cup Manager"


@app.route('/teams', methods=['GET'])
def teams():
    result = requests.get(my_api_url + "teams")
    return result.json()


@app.route('/team', methods=['POST'])
def team():
    data = request.get_json()
    headers = {'Content-Type': 'application/json'}
    response = requests.post(my_api_url + "team", data=json.dumps(data), headers=headers)
    return response.json(), 201


@app.route('/team/<id>', methods=['GET', 'PUT', 'DELETE'])
def team_by(id):
    if request.method == 'GET':
        result = requests.get(my_api_url + "team/" + id)
        return result.json()
    elif request.method == 'PUT':
        data = request.get_json()
        headers = {'Content-Type': 'application/json'}
        response = requests.put(my_api_url + "team/" + id, data=json.dumps(data), headers=headers)
        return response.json(), 201
    elif request.method == 'DELETE':
        response = requests.delete(my_api_url + "team/" + id)
        return response.json()


@app.route('/team/<id>/player', methods=['POST'])
def player(id):
    data = request.get_json()
    headers = {'Content-Type': 'application/json'}
    response = requests.post(my_api_url + "team/" + id + "/player", data=json.dumps(data), headers=headers)
    return response.json(), 201


@app.route('/team/<id>/players', methods=['GET'])
def players(id):
    result = requests.get(my_api_url + "team/" + id + "/players")
    return result.json()


@app.route('/team/<id>/player/<player_id>', methods=['GET', 'PUT', 'DELETE'])
def player_by(id, player_id):
    if request.method == 'GET':
        result = requests.get(my_api_url + "team/" + id + "/player/" + player_id)
        return result.json()
    elif request.method == 'PUT':
        data = request.get_json()
        headers = {'Content-Type': 'application/json'}
        response = requests.put(my_api_url + "team/" + id + "/player/" + player_id, data=json.dumps(data),
                                 headers=headers)
        return response.json(), 201
    elif request.method == 'DELETE':
        response = requests.delete(my_api_url + "team/" + id + "/player/" + player_id)
        return response.json()


@app.route('/competitions', methods=['GET'])
def competitions():
    result = competitionHandler.get_competitions()
    competitions_json = []

    for r in result:
        start_date = r[2].strftime("%d/%m/%Y")
        end_date = r[3].strftime("%d/%m/%Y")
        json = {
            "id": r[0],
            "name": r[1],
            "start_date": start_date,
            "end_date": end_date,
            "details": r[4],
            "number_of_teams": r[5],
            "cup_generated": r[6]
        }
        competitions_json.append(json)

    json_response = {"competitions": competitions_json}

    return json_response


@app.route('/competition', methods=['POST'])
def competition():
    data = request.get_json()
    response = competitionHandler.insert_competition(data["name"], data["start_date"], data["end_date"],
                                                     data["details"], data["num_teams"])
    return "Competition created", 201


@app.route('/junctions', methods=['GET'])
def junctions():
    result = competitionHandler.get_junctions()
    junctions_json = []

    for r in result:
        json = {
            "team_id": r[1],
            "cup_id": r[0]
        }
        junctions_json.append(json)

    json_response = {"junctions": junctions_json}

    return json_response


@app.route('/junction', methods=['POST'])
def junction():
    data = request.get_json()
    response = competitionHandler.insert_junction(data["team_id"], data["cup_id"])
    return "Junction created", 201


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    response = competitionHandler.update_generated_cup(data["generated"], data["cup_id"])
    teams = competitionHandler.get_teams_by_cup_id(data["cup_id"])
    groups = randomAPI.shuffle_teams(teams)
    for g in groups:
        competitionHandler.insert_team_in_group(data["cup_id"], teams[int(g) - 1][1])

    return "Generated", 201


@app.route('/groups', methods=['GET'])
def groups():
    result = competitionHandler.get_groups()
    groups_json = []

    group_name = 'A'
    k = 1

    for r in result:
        if k % 4 == 0:
            group_name = chr(ord(group_name) + 1)

        request = my_api_url + "team/" + str(r[1])
        team_name = requests.get(request).json()["name"]
        json = {
            "cup_id": r[0],
            "group_name": group_name,
            "team_name": team_name
        }
        groups_json.append(json)
        k += 1

    json_response = {"groups": groups_json}

    return json_response


@app.route('/sms', methods=['POST'])
def sms():
    data = request.get_json()
    smsAPI.send_message(data["message"])
    return "SMS sent", 200
