def sort_insert(A):
    """ сортировка списка А вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def sort_choise(A):
    """ сортировка списка А выбором"""
    N = len(A)
    for pos in range(0, N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def sort_bubble(A):
    """ сортировка списка А методом пузырька"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k + 1] = A[k + 1], A[k]


def test_sort(sort_def):
    print('Тестируем: ', sort_def.__doc__)
    print('#testcase #1: ', end='')
    A = [4, 2, 1, 5, 0, -7]
    A_sorted = [-7, 0, 1, 2, 4, 5]
    sort_def(A)
    print('Ok' if A == A_sorted else 'Fail')

    print('#testcase #2: ', end='')
    A = [-5, 1, -7, 2, 3, 0, 2, -5]
    A_sorted = [-7, -5, -5, 0, 1, 2, 2, 3]
    sort_def(A)
    print('Ok' if A == A_sorted else 'Fail')

    print('#testcase #3: ', end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_def(A)
    print('Ok' if A == A_sorted else 'Fail')


if __name__ == '__main__':
    test_sort(sort_insert)
    test_sort(sort_choise)
    test_sort(sort_bubble)
