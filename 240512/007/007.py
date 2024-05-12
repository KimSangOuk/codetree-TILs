class T:
    def __init__(self,code,place,time):
        self.code=code
        self.place=place
        self.time=time

c,p,k=map(str,input().split())
t=T(c,p,k)
print("secret code : "+t.code)
print("meeting point : "+t.place)
print("time : "+t.time)