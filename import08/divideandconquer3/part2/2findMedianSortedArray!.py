class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def check(nums1,nums2,k):
            #从nums1中开始尝试取数
            index1=0
            index2=0
            while True:
                if index1==len(nums1):#nums1扔完了
                    return nums2[index2+k-1]
                if index2==len(nums2):#nums1扔完了
                    return nums1[index1+k-1]
                if k==1:
                    return min(nums1[index1],nums2[index2])
                mid=(k)//2
                check_index1=min(index1+mid,len(nums1))-1
                check_index2=min(index2+mid,len(nums2))-1
                
                if nums1[check_index1]<nums2[check_index2]:#扔掉1
                    
                    k=k-(check_index1-index1+1)
                    index1=check_index1+1
                else:
                    
                    k=k-(check_index2-index2+1)
                    index2=check_index2+1
        if (len(nums1)+len(nums2))%2==1:
            return check(nums1,nums2,(len(nums1)+len(nums2))//2+1)/1.0
        else:
            return (check(nums1,nums2,(len(nums1)+len(nums2))//2)+check(nums1,nums2,(len(nums1)+len(nums2))//2+1))/2.0

        