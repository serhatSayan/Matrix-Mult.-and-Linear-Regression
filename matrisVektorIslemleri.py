
def matrixGoster(M, decimals=3):
    
        for row in M:
            print([round(x,decimals)+0 for x in row])

def sıfırMatrix(rows, cols):
        
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0.0)
    
        return M


def matrixCarp(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    C = sıfırMatrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += A[i][k] * B[k][j]
            C[i][j] = total
 
    return C

def skalerMatrisCarpim(skaler, matris):

    for i in range(len(matris)):
        for j in range(len(matris[1])):
            matris[i][j] = matris[i][j] * skaler

    return matris