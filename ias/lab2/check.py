def String_to_bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

PC_1 = [
        [57, 49,	41,	33,	25,	17,	9 ],
        [1,	58,	50,	42,	34,	26,	18],
        [10, 2,	59,	51,	43,	35,	27],
        [19, 11, 3,	60,	52,	44,	36],
        [63, 55, 47, 39, 31, 23, 15],
        [7 , 62, 54, 46, 38, 30, 22],
        [14, 6 , 61, 53, 45, 37, 29],
        [21, 13, 5 , 28, 20, 12, 4 ]
    ]

PC_2 = [
        [14,    17,	11,	24,	1,  5],
        [3 ,	28,	15,	6,	21,	10],
        [23,	19,	12,	4,	26,	8],
        [16,	7,	27,	20,	13,	2],
        [41,	52,	31,	37,	47,	55],
        [30,	40,	51,	45,	33,	48],
        [44,	49,	39,	56,	34,	53],
        [46,	42,	50,	36,	29,	32]
    ]

def doPC1(binary):
    dict = {}
    count=1
    for i in range(len(binary)):
        for j in range(len(binary[i])):
            dict[count] = binary[i][j]
            count+=1
    afterPC1 = ""
    for i in range(8):
        for j in range(7):
            afterPC1 += dict[PC_1[i][j]]

    return afterPC1


a = list(input().split())
a = "".join(a)
if len(a) <  8 :
    print("Error in the input length must be greater than 8 characters")
else:
    choice = 1
    initial_string = ""
    if len(a)>8:
        print("Which choice you want to take(1/2) ? ")
        choice = int(input())
        if choice <1 and choice >2:
            print("Error while entering choice")
            exit()

    if choice ==1:
        for i in range(8):
            initial_string+=a[i]
    else:
        a=a[::-1]
        for i in range(7,-1,-1):
            initial_string += a[i]
    binary = String_to_bits(initial_string)
    Binary_After_PC1 = doPC1(binary)
    lefthalf = Binary_After_PC1[:28]
    righthalf = Binary_After_PC1[28:]
    count = 0
    for o in range(16):
        if o == 0 or o== 1 or o==8 or o==15:
            count+=1
        else:
            count+=2

        leftdict = {}
        rightdict = {}
        start = 1
        while start<=28:
            leftdict[start]=lefthalf[(start+count-1)%28]
            rightdict[start+28] = righthalf[(start + count -1) %28]
            start+=1

        keyleft = ""
        for i in range(4):
            for j in range(6):
                keyleft += leftdict[PC_2[i][j]]
        keyright=""
        for i in range(4,8):
            for j in range(6):
                keyright += rightdict[PC_2[i][j]]
        key = keyleft+keyright
        print()
        print("Round number",str(o+1),"48bit key =====>>> ", key)