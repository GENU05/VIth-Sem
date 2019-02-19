import math
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
def algo(k,e,n):
    l = list()
    for i in range(len(k)):
        q=0
        p = ord(k[i]) 
        s=int(p) 
        while True:
            q=1
            # c = s**e % n 
            c = sq(s,e,n)
            if c==p:
                l.append(chr(s)) 
                break 
            else:
                s = c 
            # print(s,p)
            if q==100:
                print('Infinite Loop')
                return False
    
    print('CIPHER:',k)
    print('Plain:',''.join(l))
    print(enc(l,k,e,n))
    return l 

def enc(l,k,e,n): 
    m = []
    for i in range(len(l)):
        p = ord(l[i])
        # c = p ** e % n 
        c = sq(p,e,n)
        m.append(chr(c)) 
    print('Checking::',''.join(m))
    if m==list(k):
        return True 
    return False


def main():
    k = input('Cipher Text:')
    e = int(input('e: '))
    n = int(input('N: ')) 
    algo(k,e,n)


if __name__ == '__main__':
    main()