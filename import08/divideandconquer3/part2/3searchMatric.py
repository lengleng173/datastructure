from typing import List
def searchMatrix( matrix: List[List[int]], target: int) -> bool:
    if len(matrix)==0:return False
    m=len(matrix)
    n=len(matrix[0])
    a=0
    b=n-1
    while True:
        if a>=m or b<0:return False
        if matric[a][b]==target:
            return True
        if matric[a][b]>target:
            b-=1
        if matric[a][b]<target:
            a+=1


matric=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(searchMatrix(matric,5))