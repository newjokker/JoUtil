# -*- coding: utf-8  -*-
# -*- author: jokker -*-

#clinet.py
import socket
import threading

def recv(sock, addr):
    sock.sendto(name.encode('utf-8'), addr)
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))


def send(sock, addr):
    while True:
        string = input('')
        message = name + ' : ' + string
        data = message.encode('utf-8')
        sock.sendto(data, addr)
        if string.lower() == 'EXIT'.lower():
            break

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ('192.168.3.221', 9999)
    tr = threading.Thread(target=recv, args=(s, server), daemon=True)
    ts = threading.Thread(target=send, args=(s, server))
    tr.start()
    ts.start()
    ts.join()
    s.close()

if __name__ == '__main__':
    print("-----欢迎来到聊天室,退出聊天室请输入'EXIT(不分大小写)'-----")
    name = input('请输入你的名称:')
    print('-----------------%s------------------' % name)
    main()

