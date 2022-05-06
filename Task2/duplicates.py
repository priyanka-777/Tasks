def duplicates(arr,n):
	count=0
	for i in range(0,n):
		for j in range(i+1,n):
			if(arr[i]==arr[j]):
				count=count+1
	return count
arr=[]
n=int(input("enter num of values in list:"))
for i in range(0,n):
	ele=int(input("enter elements:"))
	arr.append(ele)
res=duplicates(arr,n)
if(res==0):
	print("no duplicate elements are found")
else:
	print("there are",res ,"duplicate elements")
