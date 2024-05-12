class c:
    def __init__(self,id,level):
        self.id=id
        self.level=level
a1=c("codetree","10")
u,l=map(str,input().split())
a2=c(u,l)
print("user",a1.id,"lv",a1.level)
print("user",a2.id,"lv",a2.level)