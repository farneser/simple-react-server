import socket


def load_page_from_get(request_data):
    path = request_data.split()[1]
    print(request_data)

    headers_200 = 'HTTP/1.1 200 OK\r\nContent-Type: {0}; charset: utf-8\r\n\r\n'
    headers_404 = 'HTTP/1.1 404 NotFound\r\nContent-Type: {0}; charset: utf-8\r\n\r\n'

    content_type = "text/text"

    match request_data.split('\n')[8].split()[1]:
        case 'document':
            content_type = 'text/html'
            path = "/index.html"
        case 'script':
            content_type = 'text/javascript'
        case 'style':
            content_type = 'text/css'
    try:
        with open('dist' + path, 'rb') as file:
            response = file.read()
        return headers_200.format(content_type).encode('utf-8') + response
    except FileNotFoundError:
        return headers_404.format(content_type).encode('utf-8')


def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 80))
        server.listen(4)
        print("server started")
        while True:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            client_socket.send(load_page_from_get(data))
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        print("server stopped")


if __name__ == '__main__':
    start_server()
