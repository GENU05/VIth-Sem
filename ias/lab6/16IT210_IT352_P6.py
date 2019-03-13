
def inverse(e, m) : 
    e = e % m; 
    for i in range(1, m) : 
        if ((e * i) % m == 1) : 
            return i
    return -1

def main():
    e = int(input('e: '))
    r = int(input('r: '))
    plain = input('Plaint text: ')
    p = int(input('P: '))
    q = int(input('Q: '))
    n = p * q 
    phi = (p-1)*(q-1)
    power = 1 
    while 2**(power*8) < n:
    power+=1
    power -=1
    if power ==0:
        power = 1
    blocks = []
    i=0
    while i < len(plain):
        j=0
        temp = ""
        while j<take and i<len(plain):
            j+=1
            temp += hex(ord(plain[i]))[2:]
            i+=1
        blocks.append(int(temp,16))
    # print(blocks)

    d = inverse(e,phi) 
    if d==-1 or (e*d)%phi!=1:
        print('No d value possible')
        return -1 
    





if __name__ == '__main__':
    main()