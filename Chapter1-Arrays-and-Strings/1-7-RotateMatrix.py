#https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

#uses negative indexes to set element - not elegant
def rotate_matrix(matrix):
    len_matrix = len(matrix)
    for layer in range (len_matrix // 2):
        first = layer
        last = len_matrix - layer - 1
        print("first = " + str(first))
        print("last = " + str(last))
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            print("left -> top")
            print("coordinate[" + str(layer) + "][" + str(i) + "]  -> " + "coordinate[" + str(-i - 1) + "][" + str(layer) + "]" )
            print(-i - 1)
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix
#short python style matrix rotation
def roate_matrix_alt(matrix):
    matrix[:] = zip(*matrix[::-1])
    return matrix

def main():
    print("Question 1.7\n")

    data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    data2 = [
        [1,2],
        [3,4]
    ]
    new_matrix = roate_matrix_alt(data)

    print("\n\n\n")
    for layer in new_matrix:
        print(layer)

if __name__== "__main__":
    main()