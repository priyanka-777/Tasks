def insertionsort(mylist):
	for i in range(1,len(mylist)):
		currentelement=mylist[i]
		k=i-1
		while k>=0 and mylist[k]>currentelement:
			mylist[k+1]=mylist[k]
			k=k-1
		mylist[k+1]=currentelement
arr=[]
n=int(input("enter num of values in list:"))
for i in range(0,n):
	ele=int(input("enter elements:"))
	arr.append(ele)
print("elements before sorting")
print(arr)
insertionsort(arr)
print("elements after sorting")
print(arr)
