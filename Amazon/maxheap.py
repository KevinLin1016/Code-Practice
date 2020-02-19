import heapq

listforrestaurant=[1,2,3,4,5,6,7,8,9,10]

a1=heapq.heapify(listforrestaurant)
a2=heapq.nlargest(2,listforrestaurant)
a3=heapq.nsmallest(2,listforrestaurant)
b1=heapq.heappop(a2)
