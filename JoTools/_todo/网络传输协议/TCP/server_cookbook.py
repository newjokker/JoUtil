# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from socketserver import BaseRequestHandler, TCPServer



class EchoHandler(BaseRequestHandler):
    def handle(self):
        print("got connect from", self.client_address)
        while True:
            msg = self.request.recv(1024)
            if msg[:6] == b'length':
                head_length = msg[6:12]
                print(head_length)
                print('准备循环读取')


if __name__ == "__main__":

    while True:
        serv = TCPServer(("0.0.0.0", 12211), EchoHandler)
        serv.serve_forever()










