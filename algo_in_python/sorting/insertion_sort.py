def insertion_sort(A):
    for x in range(0,len(A)):
        key = A[x]
        y = x-1
        while(y >= 0 and A[y] > key):
            A[y+1] = A[y]
            y -= 1
        A[y+1] = key 
    print(A)

insertion_sort([5,3,1,4,2])