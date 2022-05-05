def linear_search(list,n,x):
	for i in range(0,n):
		if(list[i]==x):
			return i
	return -1
arr=[]
n=int(input("enter num of values in list:"))
for i in range(0,n):
	ele=int(input("enter elements:"))
	arr.append(ele)
key=int(input("enter a value to search:"))
res=linear_search(arr,n,key)
if(res==-1):
	print("element was not present in given list")
else:
	print("element was found at index",res)
