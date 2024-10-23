     # #String

# # string="ankit,vikrant,vaibhav,rohit,sahil"
# print(string)


# string1="aditya"
# string2="chavan"
# string=string1 + string2
# print(string)

# print(string[0:3])








# #list

# list=["Army","Henry","Emma"]
# print(list)

# list=["Army","Henry","Emma"]
# for i in list:
#     print(i)



# n=int(input("Enter the number: "))
# for i in range (0,n):
#     print(i)
   


# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# l=list1+list2
# print(l)


# list3=[12,14,16,18,20]
# L=list3*2
# print(L)







# #tuple

# t1=(4,"Python",9.3,4,8,5,4)
# print(t1)


# #function on tuple

# #count
# print(t1.count(4))

# #index
# print(t1.index(9.3))







# #set

# days={"mondat","tuesday","wednesday","thursday","fridat","saturday"}
# print(days)

# #union
# day1={1,2,3,4,5}
# day2={5,6,7,8,9,10}
# print(day1.union(day2))







# #frozenset

# fs=frozenset([1,2,3,4,5])
# for i in fs:
#     print(i)





#Dictonary

Employee={"name":"jyotiraditya","Age":20,"salary":80000,"Company":"TCS"}
print(type(Employee))
print("printing employee data")
print(Employee)


#concat
def Merge(dict1,dict2):
     return (dict2.update(dict1)) 
dict1={'a':10,'b':8}
dict2={'c':12,'e':4}
print(Merge(dict1,dict2))
print(dict2)


#function
# 1
def  input(n1,n2):
    print("number 1 is: ",n1)
    print("number 2 is: ",n2)
print(input(10,20))



# 2
def num(n1,n2=20):
    print("number 1 is: ",n1)
    print("number 2 is: ",n2)

print("Passing only one argument")

num(30)

print("passing 2 arguments")
num(50,60)



def facttorial(n):
    fact=1
    if(n==0 or n==1):
        return 1

    else:
       for i in range(1,n+1):
           fact=fact*i
        
print(facttorial(5))        



#lambda function

add=lambda num:num+4
print(add(6))







      
