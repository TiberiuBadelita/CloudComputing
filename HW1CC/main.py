import Database
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class APIHandler(BaseHTTPRequestHandler):

    # ---------------------------- GET ----------------------------

    def do_GET(self):
        if self.path == '/teams':
            self.handle_teams()

        if self.path.startswith('/team/'):
            print(self.path.split('/')[2])

            if len(self.path.split('/')) > 3:
                if self.path.split('/')[3] == 'players':
                    self.handle_players(self.path.split('/')[2])
                if self.path.split('/')[3] == 'player':
                    self.handle_player(self.path.split('/')[2], self.path.split('/')[4])
            else:
                self.handle_team(self.path.split('/')[2])

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            response = '<html><body><h1 align="center">Welcome to FOOTBALL TEAMS MANAGER API!</h1></body></html>'
            self.wfile.write(response.encode())

        self.send_response(404)

    def handle_teams(self):

        response = Database.getTeams()

        json_response = []
        for team in response:
            json_response.append({
                'id': team[0],
                'name': team[1],
                'founded': team[2],
                'stadium': team[3]
            })

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        json_response = {'teams': json_response}

        self.wfile.write(json.dumps(json_response).encode())

    def handle_team(self, team_id):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = Database.getTeamById(team_id)

        if response is None:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        json_response = {
            'id': response[0],
            'name': response[1],
            'founded': response[2],
            'stadium': response[3]
        }

        self.wfile.write(json.dumps(json_response).encode())

    def handle_players(self, team_id):

        team = Database.getTeamById(team_id)

        if team is None:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        response = Database.getPlayersByTeamId(team_id)

        json_response = []

        for player in response:
            json_response.append({
                'id': player[0],
                'name': player[1],
                'age': player[2],
                'position': player[3],
                'shirt_number': player[4],
                'team_id': player[5]
            })

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        json_response = {'players': json_response}

        self.wfile.write(json.dumps(json_response).encode())

    def handle_player(self, team_id, player_id):

        response = Database.getPlayerById(player_id)

        if response is None:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        if str(response[5]) != team_id:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        json_response = {
            'id': response[0],
            'name': response[1],
            'age': response[2],
            'position': response[3],
            'shirt_number': response[4],
            'team_id': response[5]
        }

        self.wfile.write(json.dumps(json_response).encode())

        # ---------------------------- POST ----------------------------

    def do_POST(self):
        if self.path == '/team':
            self.handle_create_team()

        if self.path.startswith('/team/'):
            if len(self.path.split('/')) > 3:
                if self.path.split('/')[3] == 'player':
                    self.handle_create_player(self.path.split('/')[2])

        self.send_response(404)

    def handle_create_team(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        for key in data:
            if key not in ['name', 'founded', 'stadium']:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                return

        teams = Database.getTeams()

        for team in teams:
            if team[1] == data['name']:
                self.send_response(409, 'Team already exists')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                return

        Database.createTeam(data['name'], data['founded'], data['stadium'])

        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'team created'}
        self.wfile.write(json.dumps(response).encode())

    def handle_create_player(self, team_id):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        team = Database.getTeamById(team_id)

        if team is None:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        for key in data:
            if key not in ['name', 'age', 'position', 'shirt_number']:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                return

        players = Database.getPlayersByTeamId(team_id)

        for player in players:
            if player[1] == data['name']:
                self.send_response(409, 'Player already exists')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                return

        Database.createPlayer(data['name'], data['age'], data['position'], data['shirt_number'], team_id)

        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'player created'}
        self.wfile.write(json.dumps(response).encode())

        # ---------------------------- PUT -----------------------------

    def do_PUT(self):
        if self.path.split('/')[1] == 'team':
            if len(self.path.split('/')) == 3:
                self.handle_update_team(self.path.split('/')[2])

        if self.path.startswith('/team/'):
            if len(self.path.split('/')) > 3:
                if self.path.split('/')[3] == 'player':
                    self.handle_update_player(self.path.split('/')[2], self.path.split('/')[4])

        self.send_response(404)

    def handle_update_team(self, team_id):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        team = Database.getTeamById(team_id)

        if team is None:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        for key in data:
            if key not in ['name', 'founded', 'stadium']:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                return

        teams = Database.getTeams()

        if 'name' not in data:
            data['name'] = team[1]
        else:
            for team in teams:
                if team[1] == data['name']:
                    self.send_response(409, 'Team already exists')
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    return

        if 'founded' not in data:
            data['founded'] = team[2]

        if 'stadium' not in data:
            data['stadium'] = team[3]

        Database.updateTeam(team_id, data['name'], data['founded'], data['stadium'])

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'team updated'}
        self.wfile.write(json.dumps(response).encode())

    def handle_update_player(self, team_id, player_id):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        player = Database.getPlayerById(player_id)

        if player is None:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        if str(player[5]) != team_id:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        for key in data:
            if key not in ['name', 'age', 'position', 'shirt_number', 'team_id']:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                return

        players = Database.getPlayersByTeamId(team_id)

        if 'name' not in data:
            data['name'] = player[1]
        else:
            for player in players:
                if player[1] == data['name']:
                    self.send_response(409, 'Player already exists')
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    return

        if 'age' not in data:
            data['age'] = player[2]

        if 'position' not in data:
            data['position'] = player[3]

        if 'shirt_number' not in data:
            data['shirt_number'] = player[4]

        if 'team_id' not in data:
            data['team_id'] = player[5]

        Database.updatePlayer(player_id, data['name'], data['age'], data['position'], data['shirt_number'],
                              data['team_id'])

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'player updated'}
        self.wfile.write(json.dumps(response).encode())

        # ---------------------------- DELETE -----------------------------

    def do_DELETE(self):

        if self.path.split('/')[1] == 'team':
            if len(self.path.split('/')) == 3:
                self.handle_delete_team(self.path.split('/')[2])

        if self.path.startswith('/team/'):
            if len(self.path.split('/')) > 3:
                if self.path.split('/')[3] == 'player':
                    self.handle_delete_player(self.path.split('/')[2], self.path.split('/')[4])

        self.send_response(404)

    def handle_delete_team(self, team_id):

        team = Database.getTeamById(team_id)

        if team is None:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        Database.deleteTeam(team_id)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'team deleted'}
        self.wfile.write(json.dumps(response).encode())

    def handle_delete_player(self, team_id, player_id):

        player = Database.getPlayerById(player_id)

        if player is None:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        if str(player[5]) != team_id:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        Database.deletePlayer(player_id)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'player deleted'}
        self.wfile.write(json.dumps(response).encode())


server_address = ('', 8081)
httpd = HTTPServer(server_address, APIHandler)

print('Starting server...')
httpd.serve_forever()
