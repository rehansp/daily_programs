# reverse list without using inbuilt method
print(f'previo')
x = [1,2,3,4]
l = len(x)
x2 = []

i = -1
while(i>=-l):
  x2.append(x[i])
  print(x2)
  i-=1


# string reverse without using inbuilt method
x = "python"
l = len(x)

i = -1
while(i>=-l):
  print(x[i])
  i -=1
  
# check whether string is palindrome or not

str = "madam"
l1 = [] # empty list for forward string
l2 = [] # empty list for backward string
l = len(str)//2
print("forward")
i = 0 
while(i<l):
  print(str[i])
  l1.append(str[i])
  i+=1
x = ''.join(l1)
print("backward")


i = -1
while(i>=-l):
  print(str[i])
  l2.append(str[i])
  i-=1
y = ''.join(l2)

if x == y:
  print(f"{str} is palindrome")
else:
  print(f"{str} is not palindrome")

# remove duplicates from an array

def show_count(list):
  for x in list:
    if list.count(x)>1:
      print(f"the count of {x} is {list.count(x)}")
      list.remove(x)
      print(list)
    else:
      print("duplicates nhi hain")
show_count([1,2,3,4,5,6,7,7,8])

# swap two numbers

a = 12 
b = 10

# without using temporary variable

a = a+b
b = a - b
print("b : ",b)
a = a-b
print("a : ",a)

# Using temp

temp = a
a = b
print("a : ",a)
b = temp
print("b : ",b)


