# -*- coding: utf-8  -*-
# -*- author: jokker -*-



from socket import *
import numpy


def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]

def recv_into(arr, source):
    view = memoryview(arr).cast('B')
    while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]



if __name__ == "__main__":

    s = socket(AF_INET, SOCK_STREAM)

    c = socket(AF_INET, SOCK_STREAM)
    c.connect(('192.168.3.221', 12112))

    a = numpy.zeros(shape=5000000, dtype=float)

    print(a[:10])

    recv_into(a, c)

    print(a[:10])









