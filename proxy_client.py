import socket

BYTES_TO_READ = 4096

def get(host, port):
    requests = b"GET / HTTP1.1\www.google.com\n\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(requests)
        # Shuts down right part of socket. 
        # Client tells google that its done transmitting
        s.shutdown(socket.SHUT_WR)

        print("Waiting for response")
        chunk = s.recv(BYTES_TO_READ)
        result = b"" + chunk

        while len(chunk) > 0:
            chunk = s.recv(BYTES_TO_READ)
            result += chunk

        return result

print(get("127.0.0.1", 8080))