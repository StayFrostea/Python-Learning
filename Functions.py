# Usinheight=Nonest number of the array using builtin function
big = max({3, 2, 5, 3, 12})
print(big)

print(type(big))

big_f = float(big)

print(type(big_f))


def calculateVolume(height, width, depth):
    h = height
    w = width
    d = depth
    volume = h * w * d
    return volume


the_volume = calculateVolume(2, 4, 5)

print(the_volume)
