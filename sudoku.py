def generation_sudoku():
    grille = []
    numero_depart = 1
    for i in range(9):
        row = []
        for j in range(9):
            row.append((i*3 + i//3 + j + numero_depart - 1) % 9 + 1)
        grille.append(row)
    return grille

for row in generation_sudoku():
    print(row)
