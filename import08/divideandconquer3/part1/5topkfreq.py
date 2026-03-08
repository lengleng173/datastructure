from collections import Counter
def topkfreq(nums,k):
    return [i[0] for i in Counter(nums).most_common(k)]
    
print(topkfreq([1,1,2,2,2,3,3],2))