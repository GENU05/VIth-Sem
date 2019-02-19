#Key Generation

PC1 = [
        [57, 49,	41,	33,	25,	17,	9 ],
        [1,	58,	50,	42,	34,	26,	18],
        [10, 2,	59,	51,	43,	35,	27],
        [19, 11, 3,	60,	52,	44,	36],
        [63, 55, 47, 39, 31, 23, 15],
        [7 , 62, 54, 46, 38, 30, 22],
        [14, 6 , 61, 53, 45, 37, 29],
        [21, 13, 5 , 28, 20, 12, 4 ]
    ] 
PC2 = [
        [14,    17,	11,	24,	1,  5],
        [3 ,	28,	15,	6,	21,	10],
        [23,	19,	12,	4,	26,	8],
        [16,	7,	27,	20,	13,	2],
        [41,	52,	31,	37,	47,	55],
        [30,	40,	51,	45,	33,	48],
        [44,	49,	39,	56,	34,	53],
        [46,	42,	50,	36,	29,	32]
    ]

def one(l):
    x = ''
    for i in range(len(l)):
        x+=l[i]
    y = ''
    for i in range(len(PC1)):
        a = PC1[i]
        for j in range(len(PC1[i])):
            b = a[j] 
            y += x[b-1] 
    return y 

def step_two(x):
    # print(len(x))
    y=''
    for i in range(len(PC2)):
        a = PC2[i]
        for j in range(len(PC2[i])):
            b = a[j] 
            y += x[b-1] 
    return y 


def two(x):
    L = x[:int(len(x)/2)]
    R = x[int(len(x)/2):] 
    M = list()
    # 1, 2 , 9 , 16 
    for i in range(1,17): 
        if i == 1 or i == 2 or i == 9 or i == 16: 
            L = L[1:] + L[0] 
            R = R[1:] + R[0] 
        else:
            L = L[2:] + L[0:2] 
            R = R[2:] + R[0:2] 
        M.append( step_two(L+R) ) 
    return M 
    

def keyGeneration(x):
    l =  len(x)
    a = [int(hex(ord(x[i])),16) for i in range(l)]
    b = [format(a[i],'08b') for i in range(l)] 
    M = two( one(b) )
    # test = (input('test-case-number?:')) 
    n = 'key.txt'
    f = open(n,'w') 
    for i in range(len(M)): 
        # print('Round ',i+1 , 'Key::' ,M[i]) 
        f.write(M[i]+'\n') 
    f.close()
    
    pass 

# IP and FP

IP = [
[58, 50 ,42 ,34	,26	,18	,10	,2],
[60	,52	,44	,36	,28	,20	,12	,4],
[62	,54	,46	,38	,30	,22	,14	,6],
[64	,56	,48	,40	,32	,24	,16	,8],
[57	,49	,41	,33	,25	,17	,9	,1],
[59	,51	,43	,35	,27	,19	,11	,3],
[61	,53	,45	,37	,29	,21	,13	,5],
[63	,55 ,47 ,39	,31	,23	,15,7]
]

FP = [
[40	,8	,48	,16	,56	,24	,64	,32],
[39	,7	,47	,15	,55	,23	,63	,31],
[38	,6	,46	,14	,54	,22	,62	,30],
[37	,5	,45	,13	,53	,21	,61	,29],
[36	,4	,44	,12	,52	,20	,60	,28],
[35	,3	,43	,11	,51	,19	,59	,27],
[34	,2	,42	,10	,50	,18	,58	,26],
[33	,1	,41	,9	,49	,17	,57	,25],
]

def initial(x,l):
    # print(len(x))
    if len(x)>8:
        return initial(x[:8],l) + initial(x[8:],l+1)
    if len(x)!=8:
        r = 8 - len(x)
        for i in range(r):
            x = x + ' '
    # print(x)
    a = [int(hex(ord(x[i])),16) for i in range(8)]
    b = [format(a[i],'08b') for i in range(8)]
    c = ''
    # print('Initially block',l,':',b)
    for i in range(8):
        c = c + b[i]
    output = ''
    for i in range(8):
        for j in range(8):
            output = output + c[ IP[i][j] -1 ]
    s , e = 0 , 8
    p = []
    while e <= 64:
        p.append(int(output[s:e],2))
        s = s + 8 
        e = e + 8 
    m = ''
    # print(p)
    # print('ENCRYPTED BITS OF BLOCK:',l,end=': ')
    so = list()
    for i in range(len(x)):
        # print(x[i],'::',format(p[i],'08b'))
        so.append(format(p[i],'08b'))
    # print('Encrypted block',l,':',so)
    for i in range(len(p)):
        # p[i] = 
        m = m +chr(int(p[i])) 
    
    # print('EP Block  ',l,'::',m)
    return m
     
def final(x,l):
    # print(len(x))
    '''if len(x)>8:
        return final(x[:8],l) + final(x[8:],l+1)
    if len(x)!=8:
        r = 8 - len(x)
        for i in range(r):
            x = x + ' '
    # 
    a = [int(hex(ord(x[i])),16) for i in range(8)]
    b = [format(a[i],'08b') for i in range(8)]
    c = ''
    # print('Encrypted block',l,':',b)
    for i in range(8):
        c = c + b[i]'''
    c = x
    output = ''
    for i in range(8):
        for j in range(8):
            output = output + c[ FP[i][j] -1 ]
    s , e = 0 , 8
    p = []
    while e <= 64:
        p.append(int(output[s:e],2))
        s = s + 8 
        e = e + 8 
    m = ''
    # print(p)
    # print('ENCRYPTED BITS OF BLOCK:',l,end=': ')
    '''so = list()
    for i in range(len(x)):
        # print(x[i],'::',format(p[i],'08b'))
        so.append(format(p[i],'08b'))'''
    # print('Decrypted block',l,':',so)
    for i in range(len(p)):
        # p[i] = 
        m = m +chr(int(p[i])) 
    
    # print('FP on Block  ',l,'::',m)
    return m

# 16 Round Encryption

E = [
[32,1,2,3,4,5],
[4,5,6,7,8,9],
[8,9,10,11,12,13],
[12,13,14,15,16,17],
[16,17,18,19,20,21],
[20,21,22,23,24,25],
[24,25,26,27,28,29],
[28,29,30,31,32,1 ]
] 

P = [
[16,7,20,21,29,12,28,17],
[1,15,23,26,5,18,31,10],
[2,8,24,14,32,27,3,9],
[19,13,30,6,22,11,4,25 ]
] 

S = [
        #S1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],

        #S2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],

        #S3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],

        #S4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],

        #S5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ],

        #S6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],

        #S7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],

        #S8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
]

def f(l,k):
    # print(lenl)
    x=''
    for i in range(len(E)):
        for j in range(len(E[i])):
            # print('i:',i,'j:',j,'E:',E[i][j]-1,'L:',len(l))
            # print(l)
            x = x + l[ E[i][j] -1  ] 
    # print(x)
    y =  int(x,2) ^ int(k,2)
    # print(y) 
    # p = bin(p)[2:] 
    p = '{0:b}'.format(y)
    # print('$',len(p))
    p = '0'*(48-len(p)) + p 
    # print('%',len(p))
    final = ''
    # print(p,len(p))
    for i in range(8):
        bits_6_in_each_round = p[6*i:6*i+6] 
        # print(bits_6_in_each_round)
        row = int(bits_6_in_each_round[0] +  bits_6_in_each_round[5],2)
        # print(initial_2_bits)
        l = S[i][row] 
        last_4_digits = bits_6_in_each_round[1:5] 
        # print('*',last_4_digits)
        ans = l[int(last_4_digits,2)] 
        final = final + format(ans,'04b') 
    q = ''
    # print(int(final,2))
    for i in range(len(P)):
        for j in range(len(P[i])):
            q = q + final[ P[i][j] - 1 ] 
    return q 
     


def algo3(x,k ):
    # print(x)
    # x = bin(x)[2:]
    l = x[:32] 
    r = x[32:] 
    temp = l[:] 
    l = r[:] 
    fq = f(r,k)
    # print(temp)
    y = int(temp,2) ^ int( fq ,2)   
    n = '{0:b}'.format(y)
    n = '0'*(32-len(n)) + n
    # print(n)
    r = n   
    # print(n)
    # r = format(n,'32b')
    return l + r 


def sixteen(plaintext):
    # plaintext = open("key.txt", "r") 
    inp = plaintext
    x = ''
    for i in range(len(inp)):
        x = x + format(ord(inp[i]),'08b')
    inp = x
    key = list() 
    k = open("key.txt","r") 
    for line in k:
        # print(line)
        key.append(str(line.strip())) 
    for i in range(16):
        # print(inp,len(inp))
        inp = algo3(inp,key[i]) 
        if i!=15:
            print(inp)
    p = inp[32:]+inp[:32]
    print(p) 
    # print('-'*10)
    return p

def str_bin(x):
    p = ''
    for i in range(len(x)):
        p = p + format( int( ord(x[i]) ), '08b' ) 
    return p 

def ecb(plain,key):
    s = 0 
    e =  8 
    l = ''
    keyGeneration(key)
    f = open('output.txt','w') 
    n = len(plain) / 8 
    if n > int(n):
        n = int(n) + 1
    # print(n)
    for i in range(int(n)):
        
        # print('Palin Block',i+1,'::',plain[s:e])
        # print('In Binary',i+1,'::',str_bin(plain[s:e])) 
        ini = initial(plain[s:e],i+1) 
        # print('1==>',ini,len(ini))
        p = sixteen(ini)
        # print('2==>',p) 
        fpi = final(p,i+1) 
        print('Cipher Block',i+1,'::',str_bin(fpi))
        l = l  + fpi 
        f.write(str_bin(fpi)+'\n') 
        s = e 
        e = e + 8
    
    # print(l)


def main():
    plain = input('Plaint Text: ')
    # plain = 'Information Assurance and Security 2018'
    if len(plain) > 40:
        return 
    # elif len(plain) < 40:
    #     x = 40 - len(plain) 
    #     plain = plain + ' ' * x 
    roundkey = input('RoundKey: ') 
    # roundkey = 'CRYPTOGR'
    if len(roundkey) != 8:
        return 
    ecb(plain,roundkey)
    
    pass


if __name__ == '__main__':
    main()