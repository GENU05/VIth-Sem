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
    

def algo(x):
    l =  len(x)
    a = [int(hex(ord(x[i])),16) for i in range(l)]
    b = [format(a[i],'08b') for i in range(l)] 
    M = two( one(b) )
    test = (input('test-case-number?:')) 
    n = 'test_case'+test+'.txt'
    f = open(n,'w') 
    for i in range(len(M)): 
        print('Round ',i+1 , 'Key::' ,M[i]) 
        f.write(M[i]+'\n') 
    f.close()
    
    pass 


def main():
    x = input('Enter the input: ')
    if len(x)<8:
        print('Error. Length of string less than 8')
    elif len(x)==8:
        pass 
    else:
        print('Choose one option:\n 1. For first 8 letters\n 2. For last 8 letters')
        y = int(input('CHOICE:'))
        if y == 1 :
            x = x[:8]
        elif y==2:
            x = x[len(x)-8:]
        else:
            print('Error. Wrong choice.') 
            x=''
    if len(x)!=8:
        return -1
    print(x)
    algo(x)






if __name__ == '__main__':
    main()