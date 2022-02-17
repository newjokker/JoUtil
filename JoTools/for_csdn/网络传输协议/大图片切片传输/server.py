# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from socket import *



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

    # s.bind(('0.0.0.0', 25000))
    # s.listen(10000)
    # c,a = s.accept()

    c = socket(AF_INET, SOCK_STREAM)
    c.connect(('192.168.3.221', 12112))

    #
    # print(c)
    # print(a)

    import numpy
    a = numpy.arange(0.0, 5000000.0)
    send_from(a, c)



