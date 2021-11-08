
from Application import app

if __name__ == '__main__':
    host_name = 'localhost'
    server_port = 8888

    app.run(debug=True, host=host_name, port=server_port)

    print("Server stopped")
