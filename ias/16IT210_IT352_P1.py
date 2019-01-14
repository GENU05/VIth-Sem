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
    if len(x)>8:
        return initial(x[:8],l) + initial(x[8:],l+1)
    if len(x)!=8:
        r = 8 - len(x)
        for i in range(r):
            x = x + ' '
    print()
    a = [int(hex(ord(x[i])),16) for i in range(8)]
    b = [format(a[i],'08b') for i in range(8)]
    c = ''
    print('Initially block',l,':',b)
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
    print('Encrypted block',l,':',so)
    for i in range(len(p)):
        # p[i] = 
        m = m +chr(int(p[i])) 
    
    print('ENCRYPTED BLOCK  ',l,'::',m)
    return m
     
def final(x,l):
    if len(x)>8:
        return final(x[:8],l) + final(x[8:],l+1)
    if len(x)!=8:
        r = 8 - len(x)
        for i in range(r):
            x = x + ' '
    print()
    a = [int(hex(ord(x[i])),16) for i in range(8)]
    b = [format(a[i],'08b') for i in range(8)]
    c = ''
    print('Encrypted block',l,':',b)
    for i in range(8):
        c = c + b[i]
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
    so = list()
    for i in range(len(x)):
        # print(x[i],'::',format(p[i],'08b'))
        so.append(format(p[i],'08b'))
    print('Decrypted block',l,':',so)
    for i in range(len(p)):
        # p[i] = 
        m = m +chr(int(p[i])) 
<<<<<<< HEAD:ias/des.py
=======
    
    print('DECRYPTED BLOCK  ',l,'::',m)
>>>>>>> 368968e0fdd86af61202ca7b9539862026780559:ias/16IT210_IT352_P1.py
    return m

def main():
    s = input('Input: ')
    # des(s)
    print('-'*5,'ENCRYPTION','-'*5,'\n')
    I = initial(s,1)
    print('-'*5,'DECRYPTION','-'*5,'\n')
    F = final(I,1) 
    print('\n\n')
    print('Initial Output: ', I )
    print('\n')
    print('Final Output: ', F)

    

if __name__ == '__main__':
    main()

