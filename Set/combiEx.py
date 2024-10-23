set2=set()

print("How amny elements do you want in the set ?")
elements=int(input("Enter size :"))

i=0

while i<elements :
    val=int(input())
    set2.add(val)
    i += 1

#print("set is :",set2)

i=0

for i in set2 :
    print(i,"element is in set.")
    i += 1


print("set is :",set2)


set2.remove(3)
print("element is removed due to remove function :",set2)

set2.discard(3)
print("element is discarded due to discard function :",set2)

print("set is :",set2.copy())

set2.update([2,3,1,5,8])
print("element present in the set due to update function are :",set2)

print(set2.pop(3))








"""

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

"""