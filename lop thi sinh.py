class ThiSinh:
    def __init__(self,ten,ns,d1,d2,d3):
        self.ten=ten
        self.ns=ns
        self.d1=float(d1)
        self.d2=(float(d2))
        self.d3=float(d3)
    def tongdiem(self):
        res= "%.1f"%(self.d1+self.d2+self.d3)
        return "".join(self.ten+" "+self.ns+" "+res)
if __name__=='__main__':
    q=ThiSinh(str(input()), str(input()), str(input()), str(input()), str(input()))
    print(q.tongdiem())
