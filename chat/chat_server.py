"""
Chat room
env: Python3.6
socket fork 练习

服务端
"""

from socket import *
import os,sys
#创建网络链接
ADDR = ('0.0.0.0',8888)
#接收各种客户端请求
#
user = {}
def do_login(s,name,addr):

    if name in user or "管理员" in name:
        s.sendto("\n该用户已存在".encode(),addr)
        return
    s.sendto('ok'.encode(),addr)
    #通知其他人
    msg = f"欢迎{name}进入聊天室"
    for i in user:
        s.sendto(msg.encode(),user[i])


    #将用户加入字典
    user[name] = addr
def do_chat(s,name,text):
    msg = "%s: %s"%(name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_quit(s,name):
    msg = "%s退出了聊天室"%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto('EXIT',user[i])

        del user[name]


def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)

        msg = data.decode().split(' ')
        if msg[0] == 'L':
            do_login(s,msg[1],addr)
        elif msg[0] == 'C':
            text = ' '.join(msg[2:0])
            do_chat(s,msg[1],text)

        elif msg[0] == 'Q':
            if msg[1] not in user:
                s.sendto('EXIt'.encode(),ADDR)
                continue
            do_quit(s,msg[1])

def main():
    #套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid<0:
        return
    elif pid == 0:
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员消息:"+msg
            s.sendto(msg.encode(),ADDR)


    # 请求处理函数
    do_request(s)



if __name__ == '__main__':
    main()








