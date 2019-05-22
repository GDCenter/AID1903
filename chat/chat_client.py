"""
Chat room
env: Python3.6
socket fork 练习

客户端

"""


from socket import *
import sys,os
ip = '10.8.53.226'
ADDR = ('127.0.0.1',8888)
#创建网络链接

#创建新的进程,循环发送消息
def send_msg(name,s):
    while True:
        try:
            inf = input(">>>")
        except KeyboardInterrupt:
            inf = 'quit'

        if inf == 'quit':
            msg = "Q "+name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s"%(name,inf)
        s.sendto(msg.encode(),ADDR)



#创建新的进程,循环接收消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+"\n>>>",end='')



def main():
    s = socket(AF_INET,SOCK_DGRAM)
    while True:

        name = input("请输入网络名称:")

        msg = 'L ' + name
        s.sendto(msg.encode(),ADDR)
        result,addr= s.recvfrom(2048)
        if result.decode() == 'ok':
            print("准许进入")
            break
        else:
            print("名称已存在请重新输入:",result.decode())
    #创建新的进程
    pid = os.fork()
    if pid < 0:
        sys.exit("Error")
    elif pid == 0:
        send_msg(name,s)
    else:
        recv_msg(s)
if __name__ =='__main__':
    main()











