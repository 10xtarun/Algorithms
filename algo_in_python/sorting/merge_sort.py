def mergeSort(A):
    if(len(A) > 1):
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:] 


        mergeSort(L)
        mergeSort(R)

        i=j=k=0

        while(i<len(L) and j<len(R)):
            if(L[i]<R[j]):
                A[k]=L[i]
                i+=1 
            else:
                A[k]=R[j]
                j+=1
            k+=1

        while(i<len(L)):
            A[k]=L[i]
            i+=1 
            k+=1
        while(j<len(R)):
            A[k]=R[j]
            j+=1
            k+=1

def printList(A):
    for i in range(len(A)):
        print(A[i], end=" ")
    print()

if __name__ == '__main__':
    A = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(A)
    mergeSort(A)
    print("Sorted: ", end="\n")
    printList(A)