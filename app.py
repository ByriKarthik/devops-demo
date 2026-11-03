from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

class App(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/health":
            response = {
                "status": "healthy",
                "application": "DevOps CI/CD Demo"
            }

        elif self.path == "/":
            response = {
                "message": "Welcome to DevOps CI/CD!",
                "version": "1.0",
                "status": "running"
            }

        else:
            response = {"error": "Not found"}
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


port = int(os.environ.get("PORT", 5000))

server = HTTPServer(("0.0.0.0", port), App)

print(f"Application running on port {port}")

server.serve_forever()