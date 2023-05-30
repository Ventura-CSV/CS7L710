
def findSmallest(numbers, i):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def selectionSort(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    # numbers = list(map(int, input().split()))
    numbers = [25, 15, 5, 10, 0]
    findSmallest(numbers, 0)
    print(f'Find the 1st smallest number: {numbers}')

    findSmallest(numbers, 1)
    print(f'Find the 2nd smallest number: {numbers}')

    findSmallest(numbers, 2)
    print(f'Find the 3rd smallest number: {numbers}')

    findSmallest(numbers, 3)
    print(f'Find the 4th smallest number: {numbers}')

    findSmallest(numbers, 4)
    print(f'Find the 5th smallest number: {numbers}')
    # Code your program here

    numbers = [25, 15, 5, 10, 0]
    selectionSort(numbers)
    print(f'After call selectionSort(): {numbers}')


if __name__ == '__main__':
    main()
