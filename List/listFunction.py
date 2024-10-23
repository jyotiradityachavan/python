listEx=[]

print("How amny elements do you want in the list ?")
elements=int(input("Enter size :"))

i=0

while i<elements :
    val=int(input())
    listEx.append(val)
    i += 1

print("List is :",listEx)

i=0

while i<len(listEx) :
    print(listEx[i],"is present at index",i)
    i += 1


print(listEx.index(5))
print(listEx.pop(0))
listEx.sort()
print(listEx)
listEx.remove(5)
print(listEx)
print(listEx.count(1))
print("Copy first ",listEx.copy())
copy_variable=listEx.copy()
print("Copy second ",copy_variable)
listEx.insert(4,52)
print(listEx)
listEx.reverse()
print(listEx)
listEx.clear()
print(listEx)

