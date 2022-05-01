def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp  


def partition(a,low,high):
    pivot = a[high]
    pIndex = low

    for i in range(low,high):
        if (a[i]<=pivot):
            swap(a,i,pIndex)
            pIndex +=1

    swap(a,pIndex,high)
    return pIndex


def quicksort(a,low,high):
    if (low >= high):
        return

    pivot = partition(a,low,high)
    quicksort(a,low,pivot-1)
    quicksort(a,pivot+1,high)

if __name__ == '__main__':
 
    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    print(a)
    quicksort(a, 0, len(a) - 1)
 
    # print the sorted list
    print(a)