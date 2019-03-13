import codecs
def modInverse(e, m) : 
    e = e % m; 
    for x in range(1, m) : 
        if ((e * x) % m == 1) : 
            return x 
    return -1

def faster_modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        q = a // m 
        t = m  
        m = a % m 
        a = t 
        t = y  
        y = x - q * y 
        x = t  
    if (x < 0) : 
        x = x + m0 
    return x 

print("Enter the value of e")
e = int(input())
print("Enter the value of r")
r = int(input())
print("Enter the Plaintext")
plaintext = input()
print("Enter the value of p")
p = int(input())
print("Enter the value of q")
q = int(input())
phin = (p-1)*(q-1)
n = p*q
take = 1
while 2**(take*8) < n:
    take+=1
take -=1
if take ==0:
    take = 1
blocks = list()
i=0
while i < len(plaintext):
    j=0
    temp = ""
    while j<take and i<len(plaintext):
        j+=1
        temp += hex(ord(plaintext[i]))[2:]
        i+=1
    blocks.append(int(temp,16))
# print(blocks)
d = modInverse(e,phin)
if (e*d)%phin != 1 or d==-1:
    print("The value of d does not exist")
    exit()
count = 0
flag = 0
while count < 3:
    count += 1
    r_inverse = modInverse(r,n)
    if (r*r_inverse) % n == 1:
        flag = 1
        break
    else:
        if count ==3:
            break
        print("Enter other value of r (can't find r inverse for current r value)")
        r = int(input())
if flag == 0:
    print("The value of r inverse does not exist")
    exit()
ans = list()
count = 1
print(d)
print(blocks)
for i in blocks:
    # print("******************************Block",str(count),"******************************")
    # print(hex(i)[2:])
    count+=1
    s_dash = (i%n)*((r**e)%n) % n
    sent_signature = (s_dash**d) % n
    print("Sent signature",sent_signature)
    after_inverse = (sent_signature*r_inverse) % n
    print("Signature",after_inverse)
    convert_to_hex = hex(after_inverse)[2:]
    print(convert_to_hex)
    ans.append(convert_to_hex)
    '''
    Code for checking whether the output is coming correct or not 
    '''
    # check = after_inverse**e % n
    # if check == i:
    #     print(hex(check)[2:])
    #     print("YES")
print("All blocks hexa decimal signature value is ")
print(ans)
finalsignature = ""
count = 1
for i in ans:
    signatur = codecs.decode(i,"hex")
    signatur = "".join(map(chr, signatur))
    # signatur = ""
    # for j in range(0,len(i),2):
    #     if j+1 < len(i):
    #         value = chr(int(i[j]+i[j+1],16))
    #     else:
    #         value =  chr(int(i[j],16))
    #     signatur += value
    print("Block ",str(count)," signature :",signatur)
    finalsignature+=signatur
    count+=1
print("********************************")
print("Final signature :",finalsignature)