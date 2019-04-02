#! /usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys 
from datetime import datetime
from time import strftime
import socket


SYNACK = 0x12
RSTACK = 0x14

def checkhost(ip):
    conf.verb = 0 
    try:
        ping = srl(IP(dst=ip)/ICMP())
        print('Target Is UP. Scanning Initiated. ')
    except Exception:
        print("Couldn't reolve Target!")

def scanport(target,port):
    srcport = RandShort()
    conf.verb = 0 
    SYNACKpkt = srl(IP(dst=target)/TCP(sport=srcport,dport=port,flag="S")) 
    print(SYNACKpkt)
    pktflags = SYNACKpkt.getlayer(TCP).flags
    if pktflags == SYNACK:
        return True 
    return False         

def main():
    q = (input('Press 1 to enter Website Address. Any key for IP Address: '))
    if int(q)==1:
        target = input('Website Address [ Ex: www.google.com ] : ')
        target = socket.gethostbyname(target)
    else:
        target = input('IP : ')
    # print(target)
    min_port = int(input('Minimum port number: '))
    max_port = int(input('Maximum Port Numbrt: '))
    try:
        if int(min_port) >= 0 and int(max_port)>=0 and int(max_port) >= int(min_port):
            pass
        else:
            print('Invalid Port! Exiting...')
    except KeyboardInterrupt:
        print('Bye!')
    
    ports = range(min_port,max_port+1)
    start_clock = datetime.now()

    checkhost(target)
    # print(checkhost)
    print('Scanning....')
    count = 0
    for port in ports:
        status = scanport(target,port)
        if status == True:
            count = count + 1 
            print("Port: ",port," Open!")
    print("Total Open Ports: ",count)
    
    stop_clock = datetime.now()
    total_time = stop_clock - start_clock 
    print("Scanning Finished...")
    print("Time Taken: ",total_time)
    
if __name__ == '__main__':
    main()

