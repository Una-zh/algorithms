# -- coding: utf-8--
# author:Jing
# datetime:2019/6/26 11:36
# software: PyCharm
class Solution:
    def multiply(self, A):
        # write code here
        if A is None or len(A) == 1:
            return
        length = len(A)
        B = []
        C = [1]  # length+1
        D = [1]  # length+1
        for i in range(1, length):
            C.append(C[i-1] * A[i-1])
        for j in range(1, length):
            D.append(D[j-1] * A[length-j])
        for i in range(0, length):
            B.append(C[i] * D[length-1-i])
        return B


if __name__ == '__main__':
    a = [1,2,3,4,5]
    print Solution().multiply(a)