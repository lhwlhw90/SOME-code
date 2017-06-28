import random
def Merge(l,r):
    res=[]
    while l!=[] and r!=[]:
        if(min(l)<min(r)):
            res.append(min(l))
            l.remove(min(l))
        else:
            res.append(min(r))
            r.remove(min(r))
    if l==[]:
        res.extend(r)
    else:
        res.extend(l)
    print(res)
    return  res

def MergeSort(lst):
    if len(lst)>1:
        res1=MergeSort(lst[0:len(lst)//2])
        res2=MergeSort(lst[len(lst)//2:])
        return Merge(res1,res2)
    else:
        return lst
if __name__=='__main__':
    test=[]
    for i in range(1,11):
        a=random.randint(0,99)
        test.append(a)
    print(test)
    print(MergeSort(test))




