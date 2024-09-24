def generate_pascals_triangle(numRows):
    result = []  
    for i in range(numRows):
        currentRow = [1] * (i + 1)  
        for j in range(1, i):
            currentRow[j] = result[i-1][j-1] + result[i-1][j] 
        result.append(currentRow)
    
    return result 

n = int(input())

triangle = generate_pascals_triangle(n)

for row in triangle:
    print(row)
