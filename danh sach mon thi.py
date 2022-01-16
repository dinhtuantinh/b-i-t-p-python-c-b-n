class MonThi:
    def __init__(self,code,ten,ht):
        self.code=code
        self.ten=ten
        self.ht=ht
    def out(self):
        return self.code+" "+self.ten+" "+self.ht
if __name__=="__main__":
    res=[]
    t=int(input())
    while t>0:
        q=MonThi(str(input()),str(input()),str(input()))
        res.append(q)
        t-=1
    res.sort(key=lambda x:x.code,reverse=False)
    for i in res:
        print(i.out())