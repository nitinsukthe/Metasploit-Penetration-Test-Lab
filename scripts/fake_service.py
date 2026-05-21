sudo tee /home/victim/fake_service.py > /dev/null << 'EOF'
#!/usr/bin/env python3
import socketserver
class EchoHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(b"Welcome to Echo Service\r\n")
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            self.request.sendall(b"ECHO: " + data)
if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", 9003), EchoHandler) as server:
        server.serve_forever()
EOF