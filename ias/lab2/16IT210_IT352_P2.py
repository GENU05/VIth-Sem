def algo(x):
    l =  len(x)
    a = [int(hex(ord(x[i])),16) for i in range(l)]
    b = [format(a[i],'08b') for i in range(l)]
    pass 


def main():
    x = input('Enter the input: ')
    if len(x)<7:
        print('Error. Length of string less than 7')
    elif len(x)==7:
        pass 
    else:
        print('Choose one option:\n 1. For first 7 letters\n 2. For last s7 letters')
        y = int(input())
        if y == 1 :
            x = x[:7]
        elif y==2:
            x = x[::-1][:7]
        else:
            print('Error. Wrong choice.') 
            x=''
    if len(x)!=7:
        return -1

    algo(x)






if __name__ == '__main__':
    main()