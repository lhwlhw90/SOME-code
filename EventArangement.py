from collections import OrderedDict
class event:
    def __init__(self,p,t,d):
        self.profit=p
        self.timelimit=t
        self.description=d
"""def EventArangement(eventsquence):
    res=[]
    for x in range(0,max(eventsquence,key=lambda x:x.timelimit).timelimit):
        res.append(0)
    sorted(eventsquence,key=lambda x:x.profit)
    for x in eventsquence:
        while res[x.timelimit]!=0 and x.timelimit!=-1:
            x.timelimit=x.timelimit-1;
        if(x.timelimit==-1):
            continue
        else:
            res[x.timelimit]=x.description
    return  res
"""
def EventArangement(eventsquence):
    res=[]
    for x in range(0,max(eventsquence,key=lambda x:x.timelimit).timelimit):
        res.append(0)
    #sorted(eventsquence,key=lambda x:x.profit)
    #eventsquence.reverse()
    for x in eventsquence:
        while res[x.timelimit-1]!=0 and x.timelimit!=0:
            x.timelimit=x.timelimit-1;
        if x.timelimit==0:
            continue
        else:
            res[x.timelimit-1]=x.description
    return res

if __name__=='__main__':
    p=[35,30,25,20,15,10,5,1]
    d=[4,2,4,5,6,4,5,7]
    n=[1,2,3,4,5,6,7,8]
    eventsquence=[]
    sum=0
    for a,b,c in zip(p,d,n):
        temp=event(a,b,c)
        eventsquence.append(temp)
    print(EventArangement(eventsquence))
    for i in eventsquence:
        for s in EventArangement(eventsquence):
            if i.description==s:
                sum=i.profit+sum
    print(sum)

