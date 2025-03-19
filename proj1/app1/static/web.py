from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>My Simple Website</title>
</head>
<body>
    <div style="background-color: #333; color: white; text-align: center; padding: 15px;">
        <h1>Welcome to My Website</h1>
    </div>
    <div style="text-align: center; padding: 20px;">
        <h2>About Me</h2>
        <p>Hello! I'm [HARIKRISHNAN R]. This is my simple personal website.</p>
    </div>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()