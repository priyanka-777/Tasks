def bubblesort(list):
	n=len(list)
	for i in range(n):
		for j in range(0,n-i-1):
			if list[j]>list[j+1]:
				list[j],list[j+1]=list[j+1],list[j]
arr=[]
n=int(input("enter num of values in list:"))
for i in range(0,n):
	ele=int(input("enter elements:"))
	arr.append(ele)
print("elements before sorting")
print(arr)
bubblesort(arr)
print("elements after sorting")
print(arr)
