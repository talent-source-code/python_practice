#!/usr/bin python

import socket
from binascii import hexlify

def convert_integer():
    data = 1234

    print "Original: %x => Long host byte order: %x, Network byte ordre: %x" %(data, socket.ntohl(data), socket.htonl(data))
    print "Original: %x => Short host byte order: %x, Network byte ordre: %x" %(data, socket.ntohs(data), socket.htons(data))

if __name__ == '__main__':
    convert_integer()
