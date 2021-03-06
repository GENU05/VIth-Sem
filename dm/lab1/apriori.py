import csv 
from itertools import chain, combinations
class tup():
    def __init__(self,l,x):
        self.item = l 
        self.count = x 

def first(data,sq):
    d = dict()
    for i in range(len(data)):
        p = data[i]
        for j in range(len(p)):
            m = p[j]
            if d.get(m)==None:
                d[m] = 1 
            else:
                d[m] = d[m] + 1 
    k = list(d.items()) 
    L = list()
    for i in range(len(k)):
        p = k[i]
        # print(p)
        if p[1]>=sq:
            # print('*')
            temp = tup([p[0]],p[1])
            L.append(temp) 
    # for i in range(len(L)):
        # print(L[i].item,'::',L[i].count)
    return L
def has(d,p):
    o = set(p)
    for i in range(len(d)):
        k = d[i]
        if set(k) == o:
            return 1 
    return 0
def union(L,z):
    # print(L)
    C = list()
    d = []
    for i in range(len(L)):
        k = L[i].item
        # print(k)
        for j in range(i+1,len(L)):
            m = L[j].item 
            # print(m)
            n = list(set(k)&set(m))
            # print(n)
            if len(n) >= z:
                p = list(set(k).union(m) )
                if has(d,p) == 0 :
                    d.append(p)
                    temp = tup(p,0)
                    C.append(temp)
    # for i in range(len(C)):       
    return C
            

def debug_tup(L):
    # print(len(L))
    n = list()
    for i in range(len(L)):
        if L[i].count !=0:
            print(L[i].item,'::',L[i].count)
            n.append(L[i])
    # print(L[1]==L[0]) 
    return n 
def search(l,data):
    c = 0
    A = set(l) 
    for i in range(len(data)):
        B = set(data[i])
        if A.issubset(B) == True:
            c = c + 1 
    return c 
        


def update(data,L,sq):
    for i in range(len(L)):
        k = L[i]
        k.count = search(k.item,data)

    C = list()
    for i in range(len(L)):
        k = L[i]
        if k.count>=sq:
            C.append(k)
    # print()
    return C


def one(data,a):
    d = 0
    for i in range(len(data)):
        p = data[i]
        A = set(a)
        B = set(p)
        if A.issubset(B)==True:
            d = d + 1 
    return d 

def two(data,a,b):
    d = 0
    for i in range(len(data)):
        x = data[i] 
        A = set(a+b)
        B = set(x)
        if A.issubset(B)==True:
            d = d + 1
    return d
def algo(data,sq):
    fir = first(data,sq)
    # for i in  range(len(fir)):
        # print(fir[i].item)
    L = fir 
    last = L[:]
    # C = list() 
    c = 2 
    while True:
        print('*'*5,c,'*'*5)
        C = update(data,union(L,c-2),sq ) 
        # print(len(C))
        if len(C) <=1:
            return last 
        c += 1 
        last = C[:]
        L = C[:]



import time

def load_data(x):
    data = list()
    with open(x) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def asso(data,p,q,limit):
    if len(p)==0 or len(q)==0:
        return 
    # print(p,':',q)
    # n =two(data,p,q) 
    n = one(data,p+q)
    m =( one(data,p) )
    # print(n , ':' , m) 
    # n,m=m,n
    # print(m,':',n)
    if m!=0:
        j=n /m
    else:
        j = 0
    if (j) >= limit:
        print(p,'==>',q,':',j) 


def main():
    inq = int(input('Press 1 for retail dataset. Test Data is default'))
    if inq==1:
        a = 'retail_dataset.csv'
    else:
        a = 'test_dataset_1.csv' 
    
    data = load_data(a) 
    t = time.time()
    support_count = 5 # in percentage
    support = int ( len(data) * support_count / 100 )
    support = 10000
    L =  debug_tup( algo(data,support) )
    print('Time Taken:',time.time()-t,'sec')
    x = input('Enter 1 to see associaltion rules: ') 
    if int(x)==1:
        limit = float(input('Enter confidence limit between 0-1: '))
        print('Confidence which follows the limits is/are: ')
        '''for i in range(len(L)):
            x = L[i].item 
            if len(x)!=0:
                b = x[0] 
                for j in range(1,len(x)):
                    asso(data,x[j],b,limit) ''' 
        for i in range(len(L)):
            x = L[i].item 
            # print(x,':::',i)
            for j in range(len(x)):
                sub = list(combinations(x,j)) 
                # print(sub)
                for k in range(len(sub)):
                    a = list(sub[k]) 
                    b = list( set(x) - set(a)) 
                    asso(data,a,b,limit)

    print('Done!')
    

if __name__ == '__main__':
    main()