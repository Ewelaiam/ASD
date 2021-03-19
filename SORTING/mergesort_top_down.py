# based on wikipedia 

def mergesort(A):
    def mergesort_top_down(A, B, beg, end):
        if end - beg == 1:
            return

        mid = (end + beg) // 2

        mergesort_top_down(B, A, beg, mid)
        mergesort_top_down(B, A, mid, end)

        merge_top_down(B, A, beg, mid, end) 

    def merge_top_down(A, B, beg, mid, end):  
        i = beg
        j = mid

        for idx in range(beg, end):

            if (j == end or A[i] <= A[j]) and i < mid:
                B[idx] = A[i]
                i += 1
            else:
                B[idx] = A[j]
                j += 1

    def copy_arr(A, B): 
        for i in range(len(A)):
            B[i] = A[i]

    n = len(A)
    B = [0] * n
    copy_arr(A, B)
    mergesort_top_down(A, B, 0, n)
    return A

