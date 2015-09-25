#!/usr/bin python

import socket

def find_service_name():
    protocolname = 'tcp'
    for port in range(1,1024):
        try:
            print "Port: %s => service name %s" %(port, socket.getservbyport(port, protocolname))
        except:
#            print "Port: %s => service NULL" %port
            continue

if __name__ == '__main__':
    find_service_name()
