class Line:
    def __init__(self, code,color,second):
        self.code=code
        self.color=color
        self.second=second

code,color,second=map(str,input().split())
line=Line(code,color,second)
print("code : "+line.code)
print("color : "+line.color)
print("second : "+line.second)