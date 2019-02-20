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
def algo(k,e,n):
    l = list()
    for i in range(len(k)):
        q=0
        p = ord(k[i]) 
        s=int(p) 
        while True:
            q=1+q
            # c = s**e % n 
            c = sq(s,e,n)
            if c==p:
                l.append(chr(s)) 
                break 
            else:
                s = c 
            # print(s,p)
            if q==10**3:
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

def gcd(a, b): 
      
    # Everything divides 0  
    if (a == 0 or b == 0): 
            False
      
    # base case 
    if (a == b): 
        return a 
  
    # a is greater 
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a) 
      

def main():
    k = input('Cipher Text:')
    e = int(input('e: '))
    n = int(input('N: ')) 
    l = primeFactors(n) 
    if len(l)!=2:
        print('Incorrect p & q ')
    p , q = l[0] , l[1] 
    phi = (p-1) * (q-1)
    if gcd(phi,e)!=1:
        print('E and Phi are not co-prime.')
    algo(k,e,n)


if __name__ == '__main__':
    main()