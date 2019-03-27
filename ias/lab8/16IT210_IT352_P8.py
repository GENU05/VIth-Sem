import math
def primeFactors(n): 
    l = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        # print (2 ) 
        l.append(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            # print(i)
            l.append(i)
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        # print(n) 
        l.append(n)
    return l

#z=x^c mod n
def sq(x,c,n):
    # print("\nFormat is z=x^c mod n")
    x = int(x)
    c = int(c)
    n = int(n)

    c = '{0:b}'.format(c)

    z = 1
    l = len(c)

    for i in range(0, l):
        z = (math.pow(z, 2)) % n
        if (c[i] == "1"):
            z = (z*x) % n
    # print("z = ",int(z))
    return int(z)

def con(value):
    hex_res = hex(value)[2:]
    res = bytes.fromhex(hex_res).decode('utf-8')
    return res
def power(x, y , n): 
  
    # Initialize result 
    res = 1
      
    while (y > 0): 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % n
  
        # n must be even  
        # now y = y/2 
        y = y >> 1
          
        # Change x to x^2 
        x = (x * x) % n 
      
    return res % n 
def algo(k,e,n):
    l = list()
    # f = open("Program5-Output-CyclicProgram5.txt","w")
    f = open("q.txt","w")
    for i in range(1):
        q=0
        p = k 
        s=int(p) 
        writing = 'C'+str(0)+'= '+str(k)+'\n'
        f.write(writing)
        while True:
            q=1+q
            # c = s**e % n 
            c = pow(s,e,n) % n
            writing = 'C'+str(q)+' = '+str(c)+'\n'
            # print(writing,end='')
            f.write(writing)
            # c = sq(s,e,n)
            if c==p:
                l.append(int(s)) 
                break 
            else:
                s = c 
            # print(s,p)
            if q==10**9:
                print('Infinite Loop')
                return False
    
    print('CIPHER:',k)
    print('Plain:',l[0])
    print(enc(l[0],k,e,n))
    return l 

def enc(l,k,e,n): 
    m = []
    for i in range(1):
        p = int(l)
        # c = p ** e % n 
        c = pow(p,e,n) % n 
        # c = sq(p,e,n)
        m.append(int(c)) 
    print('Checking::',(m[0]))
    if m[0]==(k):
        return True 
    return False
import json
def import_jason():
    with open('oo.json', 'r') as f:
        distros_dict = json.load(f)

    for distro in distros_dict:
        # print(distro.keys())
        m = distro.get('_source').get('layers').get('data').get('data.data')
        print('Cipher From Shark: ',m)
    k =  m.split(':')
    x = ''
    for i in range(len(k)):
        x = x + k[i]
    return int(x,16)
from scapy.all import *
def pkmkb():
    packets = rdpcap('5.pcap')
    sessions = packets.sessions()
    text = ""
    w = ""
    for pkt in packets:
        if Raw in pkt:
            print(Raw)
            w= pkt[Raw].load
    # print(w)
    c = w.decode("utf-8")
    print(c)
    return (c)
def main():
    # k = (input('Cipher Text:').split(':'))
    # k = import_jason()
    k = int(pkmkb())
    # print(k)
    print('Integer of Cipher : ', k)
    e = int(input('e: '))
    n = int(input('N: ')) 
    # k = 104034
    # e=11
    # n=295927

    l = primeFactors(n) 
    if len(l)!=2:
        print('Incorrect p & q ')
    p , q = l[0] , l[1] 
    phi = int( (p-1) * (q-1) )
    if math.gcd(phi,e)!=1:
        print('E and Phi are not co-prime.')
    algo(k,e,n)


if __name__ == '__main__':
    main()