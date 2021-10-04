import sys


'homework array'
a = [[3,1], [1,1], [4,1], [1,2], [5,1], [9,1], [2,1], [6,1], [5,2], [3,2], [5,3], [8,1], [9,2], [7,1]]

'global counters'
n = 0

"""
recursive quicksort algorithm.
    Array a= input array (modified to be a 2D array to keep track of switches) *see homework array 'a'
    int p= first index, 0 for first itteration, modified by partition for further recursive calls 
    int r= last index, len(a)-1 for first itteration, modified by partition for further recursive calls
"""
def quicksort(a,p,r):
    'while not array of length 1'
    if p < r:
        
        'pick pivot point'
        q = partition(a, p, r)
        'print(a)'
        
        'use pivot to recursively sort'
        quicksort(a, p, q - 1) 
        quicksort(a, q + 1, r)
        print(a)

"""
pivot point picker, helper function used by recursive quicksort algorithm.
    global n= counting variable for any counting needs. do not use to keep track of values.
    Array a= input array, as provided by 'quicksort(a,p,r)'
    int p= first index, as provided by 'quicksort(a,p,r)'
    int r= last index, as provided by 'quicksort(a,p,r)'
"""
def partition(a, p, r):
    'define variables'
    global n
    x = a[p][0]
    lft = p + 1
    rgt = r
    done = False
    
    'while not sorted'
    while not done:
        'check index value and compare element values for index value and pivot value'
        while lft <= rgt and a[lft][0] <= x:
            lft = lft + 1
            n = n + 1
        
        'check length and compare element values for last index value and pivot value'
        while a[rgt][0] >= x and rgt >= lft:
            rgt = rgt - 1
            n = n + 1
            
        'when check index value surpasses length of array, stop sorting'
        if rgt < lft:
            done = True
        else:
            'else switch elements and continue'
            temp = a[lft]
            a[lft] = a[rgt]
            a[rgt] = temp
    
    'switch elements'
    temp = a[p]
    a[p] = a[rgt]
    a[rgt] = temp
    print(n)
    
    'return end of array index'
    return rgt

'function calls, below this comment is equivalent of main for Java, C, etc. '
quicksort(a, 0, len(a) - 1)
