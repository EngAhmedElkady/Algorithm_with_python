def prefix_sum(lst):
    for i in range(1,len(lst)):
        lst[i]=lst[i]+lst[i-1]






if __name__=="__main__":
    n,q=map(int,input().split())
    lst=list(map(int,input().split()))
    prefix_sum(lst)
    while q:
        x,y=map(int,input().split())
        x-=1
        y-=1    # because index equal zero
        if(x==0):  print(lst[y]);
        else:print(lst[y]-lst[x-1])