def mergesort(A):
   
    def top_down_mergesort(A, B, b, end):  
        if end - b == 1:
            return

        mid = (end + b) // 2

        top_down_mergesort(B, A, b, mid)
        top_down_mergesort(B, A, mid, end)

        top_down_merge(B, A, b, mid, end) 
 
    def top_down_merge(A, B, b, mid, end):  
        j = b
        k = mid

        for i in range(b, end):

            if (k == end or A[j] <= A[k]) and j < mid:
                B[i] = A[j]
                j += 1
            else:
                B[i] = A[k]
                k += 1

    def copy_arr(A, B):  
        for i in range(len(A)):
            B[i] = A[i]
 
    n = len(A)
    B = [0] * n
    copy_arr(A, B)
    top_down_mergesort(A, B, 0, n)
    return A