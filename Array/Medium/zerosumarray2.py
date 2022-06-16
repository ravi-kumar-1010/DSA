def insert(d,sum,li):
    d.setdefault(sum,[]).append(li)

def printallSublists(nums):
    d = {}
    insert(d,0,-1)
    print(d)
    total = 0
    for i in range(len(nums)):
        # print(i,"    ",d)
        total+=nums[i]
        if total in d:
            mylist = d.get(total)
            for starts in mylist:
                print("Found: ",starts+1,i)
        insert(d,total,i)

if __name__ == '__main__':
 
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
 
    printallSublists(nums)