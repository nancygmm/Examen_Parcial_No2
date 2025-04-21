from functools import lru_cache

keypad = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

posiciones = {}
for i in range(4):
    for j in range(3):
        val = keypad[i][j]
        if val not in ['*', '#']:
            posiciones[val] = (i, j)

movimientos = {}
for digit, (i, j) in posiciones.items():
    movimientos[digit] = [digit]  
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        ni, nj = i + dx, j + dy
        if 0 <= ni < 4 and 0 <= nj < 3:
            neighbor = keypad[ni][nj]
            if neighbor not in ['*', '#']:
                movimientos[digit].append(neighbor)

print("Diccionario de movimientos permitidos:")
for k, v in movimientos.items():
    print(f"{k} -> {v}")

@lru_cache(maxsize=None)
def caminos(d, n):
    if n == 1:
        return 1
    return sum(caminos(neigh, n-1) for neigh in movimientos[d])

def combinaciones_en_total(n):
    return sum(caminos(d, n) for d in movimientos)

print("\nCombinaciones para n = 2:", combinaciones_en_total(2))  
print("Combinaciones para n = 10:", combinaciones_en_total(10)) 
