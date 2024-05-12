class Product:
    def __init__(self,name="codetree",code="50"):
        self.name=name
        self.code=code

product1=Product()
name,code=map(str,input().split())
product2=Product(name,code)
print("product",product1.code,"is",product1.name)
print("product",product2.code,"is",product2.name)