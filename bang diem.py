import math
class BangDiem:
    def __init__(self,code,ten,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10):
        self.code="HS%02d"%code
        self.ten=ten
        self.d1=d1
        self.d2=d2
        self.d3=d3
        self.d4=d4
        self.d5=d5
        self.d6=d6
        self.d7=d7
        self.d8=d8
        self.d9=d9
        self.d10=d10
        tong=(self.d1*2+self.d2*2+self.d3+self.d4+self.d5+self.d6+self.d7+self.d8+self.d9+self.d10)/10/1.2
        s=""
        if tong>=9:
            s="XUAT SAC"
        if tong<9 and tong>=8:
            s="GIOI"
        if tong<8 and tong>=7:
            s="KHA"
        if tong<7 and tong>=5:
            s="TB"
        if tong<5:
            s="YEU"
        self.tb=tong
        self.loai=s
    def out(self):
        return "".join(self.code+" "+self.ten+" "+"{:.1f}".format(self.tb)+" "+self.loai)
t=int(input())
res=[]
for i in range(1,t+1,1):
    s=str(input())
    d=[float(x) for x in input().split()]
    q=BangDiem(i, s, d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9])
    res.append(q)
res.sort(key=lambda x:x.tb,reverse=True)
for i in res:
    print(i.out())