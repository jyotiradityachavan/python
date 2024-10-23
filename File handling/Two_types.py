file=open("demo.txt","w")
file.write("Hello everyone.")
file.close()

file=open("demo.txt","r")
#content=file.read()
print(file.read())
file.close()

with open("demo.txt","w+") as f :
    f.write("Hii\nHello\nHow are you ?")
    print(f.tell())
    f.seek(0)
    print(f.read())
    print(f.tell())
    f.seek(0)
    print(f.readline())
    print(f.tell())
    f.seek(0)
    print(f.readlines())
    print(f.tell())
    
with open("demo.txt","a") as f :
    f.write("\nI am fine")

with open("demo.txt","a+") as f :
    f.write("\nHow are you ?")
    f.seek(0)
    print(f.read())

with open("demo1.txt","x") as f :
    f.write("Ruturaj")

with open("demo2.txt","x+") as f :
    f.write("Ruturaj")
    print(f.read())


    