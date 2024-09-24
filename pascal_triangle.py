def generate_pascals_triangle(numRows):
    result = []  # Initialize the list to store rows of Pascal's triangle.

    for i in range(numRows):
        # Start each row with 1
        currentRow = [1] * (i + 1)  # Every row starts and ends with 1
        
        # For elements between the first and last one, calculate their values
        for j in range(1, i):
            currentRow[j] = result[i-1][j-1] + result[i-1][j]  # Add values from the previous row
            
        # Append the current row to the result list
        result.append(currentRow)
    
    return result  # Return the list of rows

# Example usage: Generate first 5 rows and print it as a string with each row on separate lines.
triangle = generate_pascals_triangle(5)
# print(triangle)
# Pretty print each row of Pascal's Triangle
for row in triangle:
    print(row)
