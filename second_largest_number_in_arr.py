def second_largest(arr):
    n = len(arr)
    
    if n<2:
        return "Array must contain at least two distinct element"

    largest = second_largest = float("-inf")

    for i in arr:
        if i>largest:
            second_largest = largest
            largest = i
        elif largest > i > second_largest:
            second_largest = i
        
    if second_largest == float('-inf'):
        return "There is no second largest, all elements may be the same"
    
    return second_largest


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    result = second_largest(arr)
    print(result)
