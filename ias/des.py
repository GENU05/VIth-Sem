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

def initial(x):
    if len(x)>8:
        return initial(x[:8]) + initial(x[8:])
    if len(x)!=8:
        r = 8 - len(x)
        for i in range(r):
            x = x + ' '
    a = [int(hex(ord(x[i])),16) for i in range(8)]
    b = [format(a[i],'08b') for i in range(8)]
    c = ''
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
    for i in range(len(p)):
        # p[i] = 
        m = m +chr(int(p[i])) 
    

    return m
     
def final(x):
    if len(x)>8:
        return final(x[:8]) + final(x[8:])
    if len(x)!=8:
        r = 8 - len(x)
        for i in range(r):
            x = x + ' '
    a = [int(hex(ord(x[i])),16) for i in range(8)]
    b = [format(a[i],'08b') for i in range(8)]
    c = ''
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
    for i in range(len(p)):
        # p[i] = 
        m = m +chr(int(p[i])) 
    return m

def main():
    s = input('Input: ')
    # des(s)
    I = initial(s)
    F = final(I) 
    print('Initial Output: ', I )
    print('Final Output: ', F)

    

if __name__ == '__main__':
    main()

