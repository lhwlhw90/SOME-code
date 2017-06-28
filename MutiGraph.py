class Graph:
    def __init__(self,n,i):
        self.numvex=n
        self.info=i
def MutiGraph(G,n1,n2):
    cost={n2:(0,-1)}
    for x in range(n2-1,n1-1,-1):
        if G.info[x]=={}:
            continue
        cost[x]=min([(G.info[x][i]+cost[i][0],i) for i in G.info[x].keys()])
    return cost[0],cost
if __name__=='__main__':
    g=[{1:9,2:7,3:3,4:2},{5:4,6:2,7:1},{5:2,6:7},{7:11},{6:11,7:8},{8:6,9:5},{8:4,9:3},{9:5,10:6},{11:4},{11:2},{11:5},{}]
    G=Graph(12,g)
    print(MutiGraph(G,0,11))
