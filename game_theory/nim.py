import functools


def nim_sum(arr: list) -> int:
    """
    `NIM sum = x1 ^ x2 ^ x3 ^ .... ^ xn`
    """
    return int(functools.reduce(lambda x, y: x ^ y, arr, 0))


test = [161, 274, 545, 681, 705, 84, 326, 806, 186, 508, 146, 870, 792, 737, 406, 327,
        917, 178, 194, 336, 793, 934, 929, 175, 282, 955, 658, 224, 252, 189,
        785, 413, 815, 330, 94, 521, 766, 773, 679, 305, 633, 825, 527, 778, 914, 
        933, 105, 832, 112, 652, 520, 257, 938, 449, 432, 221, 757, 442, 797, 9, 631, 582]

if nim_sum(test) == 0:
    print("Losing State")
else:
    print("Winning State")
