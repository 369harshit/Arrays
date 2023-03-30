# python Program to Insert an element
# at a specific position in an Array
def insertElement(arr, n, x, pos):
    # shift elements to the right
    # which are on the right side of pos
    for i in range(n - 1, pos - 1, -1):
        arr[i + 1] = arr[i]
    arr[pos] = x


# Driver's code
if __name__ == '__main__':
    # Declaring array and key to delete
    # here -1 is for empty space
    arr = [2, 4, 1, 8, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    n = 5

    print("Before insertion : ")
    for i in range(0, n):
        print(arr[i], end=' ')

    x = 10
    pos = 0

    # Function call
    insertElement(arr, n, x, pos)
    n += 1

    print("\nAfter insertion : ")
    for i in range(0, n):
        print(arr[i], end=' ')
