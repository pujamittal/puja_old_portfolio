import itertools

inputs = [[0, 1], [0, 1], [0, 1]]
combos = list(itertools.product(*inputs))


def nand(b0, b1):
    return int(not (b0 and b1))


def nor(b0, b1):
    return int(not (b0 or b1))

for combo in combos:
    nands = []
    a, b, c = combo
    nand0 = nand(a, b)
    nand1 = nand(nand0, 1)
    nand2 = nand(nand0, 0)
    nand3 = nand(nand1, c)
    nand4 = nand(nand2, c)
    nand5 = nand(nand3, 1)
    nand6 = nand(nand4, 0)
    print(a, b, c, nand0, nand1, nand2, nand3, nand4, nand5, nand6)


for combo in combos:
    a, b, c = combo
    nand0 = nand(a, b)
    nand1 = nand(nand0, 1)
    nand2 = nand(nand1, c)
    nand3 = nand(nand2, 1)
    print(a, b, c, nand3)


for combo in combos:
    a, b, c = combo
    nor0 = nor(a, a)
    nor1 = nor(b, b)
    nor2 = nor(c, c)
    nor3 = nor(nor0, nor1)
    nor4 = nor(nor1, nor2)
    nor5 = nor(nor3, nor3)
    nor6 = nor(nor4, nor4)
    nor7 = nor(nor5, nor6)
    print(a, b, c, nor0, nor1, nor2, nor3, nor4, nor5, nor6, nor7)
