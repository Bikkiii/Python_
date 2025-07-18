def names(name,address):        #parameter
    print(f"Hello!, {name} and you lives in {address}?")
    print(f"what's up!, {name} and he lives in {address}")
    print(f"How do you do, {name} and he lives in {address}")
names("Mama","Hostel")           #passing_argument
# names("Nobita","Sinamangal")
# names("Niggs","Bhaktapur")

def hello(a,b,c):
    print(a,b,c)
hello(1,2,3)    
hello(b=2,a=1,c=3)      #keyword arguments

def names(name,address):        #parameter
    print(f"Hello!, {name} and you lives in {address}?")
    print(f"what's up!, {name} and he lives in {address}")
    print(f"How do you do, {name} and he lives in {address}")
names(address="Hostel",name="Mama")   