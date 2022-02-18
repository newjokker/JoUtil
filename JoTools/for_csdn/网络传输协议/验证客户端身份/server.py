# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import hmac
import os
from socket import socket, AF_INET, SOCK_STREAM

secret_key = b'peekaboo'


def client_authenticate(connection, secret_key):
    message = connection.recv(32)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    connection.send(digest)

def server_authenticate(connection, secret_key):
    message = os.urandom(32)
    connection.send(message)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest, response)


def echo_handler(client_sock):
    if not server_authenticate(client_sock, secret_key):
        client_sock.close()
        return
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)

def echo_servre(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    while True:
        c,a = s.accept()
        echo_handler(c)




if __name__ == "__main__":


    echo_servre(('0.0.0.0', 11221))









