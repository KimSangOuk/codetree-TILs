n=int(input())

class Person:
    def __init__(self,name,port,region):
        self.name=name
        self.port=port
        self.region=region
    
person_list=list()
last_name=""
last_index=-1
for i in range(n):
    name,port,region=map(str,input().split())
    if name>last_name:
        last_name=name
        last_index=i
    person_list.append(Person(name,port,region))

print("name",person_list[last_index].name)
print("addr",person_list[last_index].port)
print("city",person_list[last_index].region)