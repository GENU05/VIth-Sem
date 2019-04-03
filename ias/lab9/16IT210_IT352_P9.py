import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys 
from datetime import datetime
from time import strftime
import socket

f = open('Program9-Output.txt','w')

SYNACK = 0x12
RSTACK = 0x14

def checkhost(ip):
    conf.verb = 0 
    try:
        ping = sr1(IP(dst=ip)/ICMP(),timeout=10)
        if ping == None:
            text = "Couldn't reolve Target!"
            f.write(text+'\n')
            print(text)
            return False
        text = 'Target Is UP. Scanning Initiated. '
        f.write(text+'\n')
        print(text)
        return True
    except Exception:
        text = "Couldn't reolve Target!"
        f.write(text+'\n')
        print(text)
        return False

def TCP_REQ(target,port):
    srcport = RandShort()
    conf.verb = 0 
    SYNACKpkt = sr1( IP( dst=target ) / TCP( sport=srcport,dport=port,flags="S" ) , timeout=2 ) 
    # print(SYNACKpkt)
    if(SYNACKpkt==None):
        # print('Port ', port,' Filtered!')
        return False
    # pktflags = SYNACKpkt.getlayer(TCP).flags
    if(SYNACKpkt.getlayer(TCP)):
        if(SYNACKpkt.getlayer(TCP).flags==SYNACK):
            # Send RST.
            i = send( IP(dst=target) / TCP(sport=srcport,dport=port,flags="RA") )
            m = SYNACKpkt[0].show()
            # f.write(m)
            return True
        elif(SYNACKpkt.getlayer(TCP).flags==RSTACK):
            return False
    # Control ICMP response.
    elif(SYNACKpkt.haslayer(ICMP)):
        if(int(SYNACKpkt.getlayer(ICMP).type)==3 and int(SYNACKpkt.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            # print('Port ', port,' Filtered!')
            return False
    # print('Port ', port,' Unknown!')
    return False
    # if pktflags == SYNACK:
    #     return True 
    # return False 
def TCP_ACK(target,port):
    # print('Scanning Port Number: ',port)
    srcport = RandShort()
    conf.verb = 0 
    SYNACKpkt = sr1( IP( dst=target ) / TCP( sport=srcport,dport=port,flags="S" ) , timeout=2 ) 
    # print(SYNACKpkt)
    if(SYNACKpkt==None):
        # print('Port ', port,' Filtered!')
        return False
    # pktflags = SYNACKpkt.getlayer(TCP).flags
    if(SYNACKpkt.getlayer(TCP)):
        if(SYNACKpkt.getlayer(TCP).flags==SYNACK):
            # Send RST.
            i = send( IP(dst=target) / TCP(sport=srcport,dport=port,flags="R") )
            m = SYNACKpkt[0].show()
            # f.write(SYNACKpkt[0])
            return True
        elif(SYNACKpkt.getlayer(TCP).flags==RSTACK):
            return False
    # Control ICMP response.
    elif(SYNACKpkt.haslayer(ICMP)):
        if(int(SYNACKpkt.getlayer(ICMP).type)==3 and int(SYNACKpkt.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            # print('Port ', port,' Filtered!')
            return False
    # print('Port ', port,' Unknown!')
    return False
        

def main():
    q = (input('Press 1 to enter Website Address. Press 2 for IP Address: '))
    if int(q)==1:
        target = input('Website Address [ Ex: www.google.com ] : ')
        target = socket.gethostbyname(target)
    else:
        target = input('IP : ').strip()
    print(target,len(target))
    f.write('Target : '+ str(target)+'\n')
    # min_port = int(input('Minimum port number: '))
    # max_port = int(input('Maximum Port Numbrt: '))
    # try:
    #     if int(min_port) >= 0 and int(max_port)>=0 and int(max_port) >= int(min_port):
    #         pass
    #     else:
    #         print('Invalid Port! Exiting...')
    # except KeyboardInterrupt:
    #     print('Bye!')
    # # print()
    q = int(input('For TCP ACK SYNC Method press 1. Press 2 for TCP REQ Method: '))
    
    # ports = range(min_port,max_port+1)
    ports = [20,21,22,80,443]
    start_clock = datetime.now()

    if checkhost(target) == False:
        text = 'Quiting...'
        f.write(text+'\n')
        print(text)
        # print()
        return False
    # print(checkhost)
    text = 'Scanning....'
    f.write(text+'\n')
    print(text)
    # print()
    count = 0
    total = 0
    for port in ports:
        total = total + 1 
        if q==1:
            status = TCP_ACK(target,port)
        else:
            status = TCP_REQ(target,port)
        if status == True:
            count = count + 1 
            text = ("Port: "+str(port)+" Open!")
            f.write(text+'\n')
            print(text)
        if total % 500 == 0:
            text = ('Scanned Ports Till Now: '+str(total))
            f.write(text+'\n')
            print(text)
    text = "Total Open Ports: "+str(count)
    f.write(text+'\n')
    print(text)
    
    stop_clock = datetime.now()
    total_time = stop_clock - start_clock 
    text = ("Scanning Finished...")
    f.write(text+'\n')
    print(text)
    text = ("Time Taken: "+str(total_time))
    f.write(text+'\n')
    print(text)
    
if __name__ == '__main__':
    main()

