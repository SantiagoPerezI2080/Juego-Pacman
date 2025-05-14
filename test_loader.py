from services.level_loader import LevelBuilder

if __name__ == '__main__':
    walls, food, entities = LevelBuilder('assets/map.txt').build()
    print('Matriz de muros:')
    for row in walls:
        print(''.join(str(cell) for cell in row))
    print('\nPosiciones de comida:', food)
    print('\nEntidades cargadas:', [type(e).__name__ for e in entities])
