# Time Complexity :- BigO(N) as we are traversing the array only once.
#
# Space Complexity :- BigO(1) as we are not using any extra space
class Solution:
    def validMountainArray(self, arr):
        if len(arr) <3:
            return False
        low =0
        high = len(arr) -1 #finding 2nd highest index

        #traversing low to high part
        while low+1 < high and arr[low] < arr[low+1]:
            low = low+1

        #Traversing high to low part
        while high-1 >0 and arr[high] < arr[high-1]:
            high = high -1

        if low == high:
            return True