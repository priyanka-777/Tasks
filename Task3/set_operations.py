def union(arr1,arr2):
	result=list(set(arr1+arr2))
	print("union of given lists is:",result)
def intersection(arr1,arr2):
	temp=set(arr2)
	list=[value for value in arr1 if value in temp]
	print("intersection of given lists is:",list)
def difference(arr1,arr2):
	res=list(set(arr1)-set(arr2))
	print("difference between",arr1,"and",arr2,"is",res)
arr1=[]
arr2=[]
m=int(input("enter num of values in list1:"))
for i in range(0,m):
	ele=int(input("enter elements into first list:"))
	arr1.append(ele)
print("first list")
print(arr1)
n=int(input("enter num of values in list2:"))
for i in range(0,n):
	ele=int(input("enter elements into list2:"))
	arr2.append(ele)
print("second list")
print(arr2)
union(arr1,arr2)
intersection(arr1,arr2)
difference(arr1,arr2)
difference(arr2,arr1)
