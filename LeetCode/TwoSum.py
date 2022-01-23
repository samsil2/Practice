#Complexity O(n)

def two_sum(arr,targ):
    dict = {}
    for i, num in enumerate(arr):
        if targ-num in dict.keys():
            return [dict[targ-num], i]
        else:
            dict[num] = i



a = (2,7,1,15)
t = 9
print(two_sum(a,t))  # (0,1)

a = (-3,4,3,90)
t = 0
print(two_sum(a,t))  # (0,2)
