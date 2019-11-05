def zero_matrix(matrix):

    if len(matrix) <= 0 or len(matrix[0]) <= 0:
        return False
     
    lenOfRow = len(matrix[0])
    lenOfCol = len(matrix)

    #keep track of which rows/cols to zero

    rows = []
    cols = []

    for i in range(lenOfCol):
        for j in range (lenOfRow):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)
    
    #need to zero row separately in order to not zero out areas due to the next index == 0 
    for row in rows:
        zero_row(matrix, row)

    for col in cols:
        zero_column(matrix, col)

    return matrix

def zero_row(matrix, row):
    lenOfRow = len(matrix[0])
    
    for i in range(lenOfRow):
        matrix[row][i] = 0

def zero_column(matrix, col):
    lenOfCol = len(matrix)

    for i in range (lenOfCol):
        matrix[i][col] = 0


def main():
    print("Question X.X\n")
    data = [
        [0, 2, 3],
        [4, 0, 6],
        [7, 8, 9],
        [1,3,4]
    ]

    new_matrix = zero_matrix(data)

    print("\n\n\n")
    for layer in new_matrix:
        print(layer)

if __name__== "__main__":
    main()