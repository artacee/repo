grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

diagonal = [row[index] for index, row in enumerate(grid)]
print(diagonal)
