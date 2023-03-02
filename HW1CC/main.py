from http.server import BaseHTTPRequestHandler, HTTPServer
import json, Database


class APIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/teams':
            self.handle_teams()

        if self.path.startswith('/team/'):
            print(self.path.split('/')[2])

            if len(self.path.split('/')) > 3:
                if self.path.split('/')[3] == 'players':
                    self.handle_players(self.path.split('/')[2])

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

        self.wfile.write(json.dumps(response).encode())

    def handle_team(self, team_id):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = Database.getTeamById(team_id)

        self.wfile.write(json.dumps(response).encode())

    def handle_players(self, team_id):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'players'}
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == '/team':
            self.handle_create_team()

    def handle_create_team(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        Database.createTeam(data['name'], data['founded'], data['stadium'])

        response = {'message': 'team created'}
        self.wfile.write(json.dumps(response).encode())


server_address = ('', 8081)
httpd = HTTPServer(server_address, APIHandler)

print('Starting server...')
httpd.serve_forever()
