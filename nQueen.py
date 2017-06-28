"""class ChessBoard:
    def __init__(self,s):
        self.scale=s
        self.info=[]
        for i in range(s):
            self.info.append([])
            for p in range(s):
                self.info[i].append(0)
        print(self.info)
def feasible(CB,start,p):
    s=[s[p] for s in CB.info]
    tem=[g for g in CB.info[start]]
    del s[start]
    del tem[p]
    if (1 in s)or(1 in tem):
        return False
    else:
        for m in range(len(CB.info)):
            for i in range(len(CB.info[m])):
                if CB.info[m][i] == 1 and abs(m - start) == abs(p - i):
                    return False
                else:
                    return True
def nQueen(CB,start=0):
    for p in range(0,len(CB.info[start])):
        print(start,p)
        CB.info[start][p] = 1
        if feasible(CB,start,p):
            print((start,p))
            if CB.scale==start+1:
                print(CB.info)
                exit(0)
            nQueen(CB,start+1)
        else:
            CB.info[start][p] = 0
            continue
    CB.info[start-1][CB.info[start-1].index(1)]=0
if __name__=="__main__":
    CB=ChessBoard(8)
    nQueen(CB,0)
    """
"""ans=[-1,-1,-1,-1,-1,-1,-1,-1]
def place(s,j):
    for k in range(s):
        if ans[k]==j or abs(k-s)==abs(ans[k]-j):
            return False
        return True

def nQ(d,):
    r=0
    c=0
    while r<len(ans):
        while c<len(ans):
            if place(r,c):
                ans[r]=c
                c=0
                break
            else:
                c=c+1
        if ans[r]==-1:
            if r==0:
                break
            else:
                r=r-1
                c=ans[r]+1
                ans[r]=-1
                continue
        if r==len(ans)-1:
            c=ans[r]+1
            ans[r]=-1
            continue
        r=r+1
        return
print(ans)
nQ(ans)
print(ans)
"""
from itertools import *
cols=range(8)
for vector in permutations(cols):
    if(8==len(set(vector[i]+i for i in cols))==len(set(vector[i]-i for i in cols))):
        print(vector)