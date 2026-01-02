ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()

# program crashes with error message
assert ages[0] <= ages[-1], "Ages is not sorted, last value > than first."