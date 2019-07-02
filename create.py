def creator():
    matrix = []
    for r in range(3):
        matrix.append([])
        for c in range(8):
            if c%2 == r%2:
                matrix[r].append("o")
            else:
                matrix[r].append(0)
    for r in range(3,5):
        matrix.append([])
        for c in range(8):
            matrix[r].append(0)
    for r in range(5,8):
        matrix.append([])
        for c in range(8):
            if c%2 == r%2:
                matrix[r].append("x")
            else:
                matrix[r].append(0)
    return matrix
    
creator()
