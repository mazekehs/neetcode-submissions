class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)> len(nums2):
            nums1,nums2=nums2,nums1
        
        A,B=nums1,nums2
        total=len(A)+len(B)
        half=total//2

        l,r=0,len(A)

        while True:
            i=(l+r)//2
            j=half-i

            if i>0:
                Aleft=A[i-1]
            else:
                Aleft=float("-inf")
            if i<len(A):
                Aright=A[i]
            else:
                Aright=float("inf")
            
            if j>0:
                Bleft=B[j-1]
            else:
                Bleft=float("-inf")
            if j<len(B):
                Bright=B[j]
            else:
                Bright=float("inf")
            

            if Aleft<=Bright and Bleft<=Aright:

                if total%2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1

            
            

        