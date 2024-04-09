import socket
import http.server

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 8000        # Port to listen on (non-privileged ports are > 1023)


def run():
    """Starts the HTTP server and listens for requests."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Serving at http://{HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            print('Connected by', addr)  # Consistent indentation

            with conn:
                print(f'Connected by {addr}')
                # Simplistic request handling (replace with actual processing)
                request = conn.recv(1024).decode('utf-8')
                response = f"HTTP/1.1 200 OK\n\nHello, World!\n"
                conn.sendall(response.encode('utf-8'))


if __name__ == '__main__':
    run()
