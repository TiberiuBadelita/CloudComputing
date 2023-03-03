from http.server import BaseHTTPRequestHandler, HTTPServer
import json, Database


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

    def handle_teams(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = Database.getTeams()

        json_response = []
        for team in response:
            json_response.append({
                'id': team[0],
                'name': team[1],
                'founded': team[2],
                'stadium': team[3]
            })

        json_response = {'teams': json_response}

        self.wfile.write(json.dumps(json_response).encode())

    def handle_team(self, team_id):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = Database.getTeamById(team_id)

        json_response = {
            'id': response[0],
            'name': response[1],
            'founded': response[2],
            'stadium': response[3]
        }

        self.wfile.write(json.dumps(json_response).encode())

    def handle_players(self, team_id):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

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

        json_response = {'players': json_response}

        self.wfile.write(json.dumps(json_response).encode())

    def handle_player(self, team_id, player_id):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

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

    def handle_create_team(self):
        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        Database.createTeam(data['name'], data['founded'], data['stadium'])

        response = {'message': 'team created'}
        self.wfile.write(json.dumps(response).encode())

    def handle_create_player(self, team_id):
        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        Database.createPlayer(data['name'], data['age'], data['position'], data['shirt_number'], team_id)

        response = {'message': 'player created'}
        self.wfile.write(json.dumps(response).encode())

        # ---------------------------- PUT -----------------------------

    def do_PUT(self):
        if self.path.split('/')[1] == 'team':
            self.handle_update_team(self.path.split('/')[2])

        if self.path.startswith('/team/'):
            if len(self.path.split('/')) > 3:
                if self.path.split('/')[3] == 'player':
                    self.handle_update_player(self.path.split('/')[2], self.path.split('/')[4])

    def handle_update_team(self, team_id):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

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

        if 'name' not in data:
            data['name'] = team[1]

        if 'founded' not in data:
            data['founded'] = team[2]

        if 'stadium' not in data:
            data['stadium'] = team[3]

        Database.updateTeam(team_id, data['name'], data['founded'], data['stadium'])

        response = {'message': 'team updated'}
        self.wfile.write(json.dumps(response).encode())

    def handle_update_player(self, team_id, player_id):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        Database.updatePlayer(player_id, data['name'], data['age'], data['position'], data['shirt_number'], team_id)

        response = {'message': 'player updated'}
        self.wfile.write(json.dumps(response).encode())


server_address = ('', 8081)
httpd = HTTPServer(server_address, APIHandler)

print('Starting server...')
httpd.serve_forever()
