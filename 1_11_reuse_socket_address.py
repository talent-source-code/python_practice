#!/usr/bin python

import socket
import sys

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "old sock state: %s" %old_state

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "new sock state: %s" %new_state

    local_port = 8283

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    srv.bind(('127.0.0.1',local_port))
    srv.listen(1)
    print "Listening on port: %s" %local_port


    while True:
        try:
            connection, addr = srv.accept()
            print "Connected by %s:%s" %(addr[0],addr[1])
        except KeyboardInterrupt, e:
            print "keyboard interupt"
            break
        except socket.error, msg:
            print "%s" %(msg,)
            break

if __name__ == '__main__':
    reuse_socket_addr()
