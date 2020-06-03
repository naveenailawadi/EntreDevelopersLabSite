from flaskapp import app
import socket

if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print('running')
    app.run(debug=True, host='127.0.0.1')
