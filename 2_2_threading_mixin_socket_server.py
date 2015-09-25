#!/usr/bin python

#import os
from socket import *
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024

def client(ip, port, message):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE)
        print "Client received: %s" %response
    finally:
        sock.close()

class ThreadTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        current_thread = threading.current_thread()
        response = "%s: %s" %(current_thread, data)
        self.request.sendall(response)

class ThreadTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def main():
    server = ThreadTCPServer((SERVER_HOST, SERVER_PORT), ThreadTCPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target = server.serve_forever)
    server_thread.setdaemon = True
    server_thread.start()
    print "Server loop running on thread: %s" %server_thread.name

    client(ip, port, "hello from client 1")
    client(ip, port, "hello from client 2")
    client(ip, port, "hello from client 3")

    server.shutdown()

if __name__ == '__main__':
    main()
