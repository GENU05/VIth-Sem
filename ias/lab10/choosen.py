
# f = open('Program7-Output-BlindSignature.txt','w')
def inverse(e, m) : 
    e = e % m; 
    for i in range(1, m) : 
        if ((e * i) % m == 1) : 
            return i
    return -1

def con(value):
    hex_res = hex(value)[2:]
    res = bytes.fromhex(hex_res).decode('utf-8')
    return res
def blind_attack(n,phi,blocks,r,ir,d,e):
    ans = list() 
    c = 1 
    m = 0 
    for i in blocks:
        text = '-'*5+'Block:'+str(c)+'-'*5 +'\n'
        # f.write(text)
        print(text)
        c = c + 1 

        text = 'Block Value: '+ str(con(i))
        # f.write(text+'\n')
        print(text)

        text = 'Initial Block (m) :' + str(i)
        # f.write(text+'\n')
        print(text)

        #encrypting plain text
        # iI = i ** e % n 
        iI = i 

        #-----------------
        s =  (iI%n)* ((r**e)%n) % n 
        text = "m' : " + str(s) 
        # f.write(text+'\n')
        print(text) 

        sentS = s**d % n 
        text = "m''  " + str(sentS) 
        # f.write(text+'\n')
        print(text)

        # apply inverse 
        iS = (sentS * ir ) % n 
        text = 'Plain: ' + str(iS)
        # f.write(text+'\n')
        print(text)

        # text = 'm(check): ' + str(iS**e%n)
        # f.write(text+'\n')
        # print(text)

        # text = 'Decrypted Block: '+ str(con(iS**e%n))
        # f.write(text+'\n') 
        # print(text) 

        if  iS**e%n !=i: # iS !=i:
            m = 1 
            print("Unsuccessfull")
            # f.write('\nUnsuccessfull\n')
            return -1
        # iS = iS**e % n 
        p = hex(iS)[2:]
        # print(p)
        ans.append(p)
    if m==0:
        print('\n')
        print("Successful")
        # f.write('\nSuccessful\n')
    print('All Blocks [In Hex] :\n',ans) 
    return ans

def final(ans):
    fs = ""
    count = 1 
    if type(ans) == int:
        return 
    for i in ans:
        s = ""
        for j in range(0,len(i),2):
            if j+1 < len(i):
                value = chr(int(i[j]+i[j+1],16))
            else:
                value =  chr(int(i[j],16))
            s += value
        # print("Block ",str(count)," Value :",s)
        fs+=s
        count+=1
    print("-"*50)
    text = 'Final Output: ' + str(fs) +'\n'
    # f.write(text)
    print("Final Output :",fs)
    return fs 

def size(n):
    power = 1 
    while 2**(power*8) < n:
        power = power + 1
    power = power - 1
    if power ==0:
        power = 1 
    return power
from math import gcd
def main(p,q,r,e,plain):
    # test = int(input('Test-Case: '))
    # text = '$'*5 + '-'*5 + 'Test Case - ' + str(test) +  '-'*5 + '$'*5 + '\n'
    # f.write(text)
    
    # p = int(input('P: '))
    # q = int(input('Q: '))

    n = p * q 
    phi = (p-1)*(q-1)
    # r = int(input('r: '))
    # e = int(input('e: '))
    
    
    
    # plain = input('Cypher text: ')
    
    if gcd(e,phi)!=1:
        print("E and Phi are not co-prime")
        return -3 
    
    power = size(n)
    # print(power)
    blocks = []
    i=0
    while i < len(plain):
        j=0
        temp = ""
        while j<power and i<len(plain):
            j+=1
            temp += hex(ord(plain[i]))[2:]
            i+=1
        blocks.append(int(temp,16))
    # print(blocks)

    d = inverse(e,phi) 
    if d==-1 or (e*d)%phi!=1:
        text = 'No d value possible'
        # f.write(text+'\n')
        print(text)
        return -1 
    
    ir = inverse(r,n) 
    if ir==-1 or (ir*r)%n != 1 :
        text = 'No r possible'
        # f.write(text+'\n')
        print(text)
        return -2 

    ans = blind_attack(n,phi,blocks,r,ir,d,e) 
    # return final(ans)
    return ans 


if __name__ == '__main__':
    main()