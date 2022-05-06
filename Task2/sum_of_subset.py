def subset(arr,n,key):
	for i in range(0,n):
		for j in range(1,n):
			if(arr[i]+arr[j]==key):
				print("values are",arr[i],",",arr[j])
				return 1
				break
				
arr=[]
n=int(input("enter num of values in list:"))
for i in range(0,n):
	ele=int(input("enter elements:"))
	arr.append(ele)
key=int(input("enter a value to search:"))
res=subset(arr,n,key)
if(res==1):
	print("elements are found")
else:
	print("there are no values present in given array which equals to given key")
