import csv 

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
                d[m] += 1 
    k = list(d.items()) 
    L = list()
    for i in range(len(k)):
        p = k[i]
        if p[1]>=sq:
            temp = tup([p[0]],p[1])
            L.append(temp)
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
    for i in range(len(L)):
        print(L[i].item,'::',L[i].count)
    # print(L[1]==L[0])

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



def algo(data,sq):
    fir = first(data,sq)
    # for i in  range(len(fir)):
        # print(fir[i].item)
    L = fir 
    last = L[:]
    # C = list() 
    c = 2 
    while True:
        C = update(data,union(L,c-2),sq ) 
        # print(len(C))
        if len(C) <=1:
            return last 
        c += 1 
        last = C[:]
        L = C[:]





def load_data(x):
    data = list()
    with open(x) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def main():
    # a = 'test_dataset_1.csv' 
    a = 'retail_dataset.csv'
    data = load_data(a)
    debug_tup( algo(data,2) )

if __name__ == '__main__':
    main()