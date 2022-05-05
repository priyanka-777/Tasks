def binarysearch(arr,low,high,x):

	if high>=low:
		mid=(high+low)//2
		if arr[mid]==x:
			return mid
		elif arr[mid]>x:
			return  binarysearch(arr,low,mid-1,x)
		else:
			return binarysearch(arr,mid+1,high,x)
	else:
		return -1
arr=[]
n=int(input("enter num of values in list:"))
for i in range(0,n):
	ele=int(input("enter elements:"))
	arr.append(ele)
key=int(input("enter a value to search:"))
result=binarysearch(arr,0,n-1,key)
if result!=-1:
	print("element is present at %d"%result)
else:
	print("element is  not present in array")
		
