def search(l,n):
    end = len(l) - 1
    start = 0
    count = 1
    while start <= end:  
        middle = (start + end) // 2  

        if l[middle] == n:
            return middle
        
        elif l[middle] > n:
            end = middle - 1

        elif l[middle] < n:
            start = middle + 1
        count+=1

print(search([1,4,8,9,12,14,23,44,55,65,76,77,79,84,85,91,92,93,94],14))   
