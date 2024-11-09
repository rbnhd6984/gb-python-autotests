# Игра орел и решка
from random import randint, choice

length = randint(1, 101)
coins = [choice([0, 1]) for _ in range(length)]
heads = coins.count(0)
tails = coins.count(1)

if heads > tails:
    print(f'Выпало {heads} орла и {tails} решка, победил орел')
elif heads < tails:
    print(f'Выпало {heads} орла и {tails} решка, победил решка')
else:
    print(f'Выпало {heads} орла и {tails} решка, ничья')
