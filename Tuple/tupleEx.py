tupleEx=()

print("How amny elements do you want in the tuple ?")
elements=int(input("Enter size :"))

i=0

while i<elements :
    val=int(input())
    tupleEx += (val,) 
    i += 1

print("List is :",tupleEx)

i=0

while i<len(tupleEx) :
    print(tupleEx[i],"is present at index",i)
    i += 1


print(tupleEx.index(5))

print(tupleEx.count(1))
