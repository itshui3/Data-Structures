# matrix problems

# given a 6 x 6 2d array

# do this recursively and show off implementation to heather

def hourglassSum(arr):
    # we're only dealing with 6x6 matrices

    # arr = outer array of 6 arrays
    x = 0
    y = 0
    maximum = sum_hourglass(arr, { 'x': x, 'y': y })

    for y in range(0, len(arr)-2):

        for x in range(0, len(arr)-2):

            new_val = sum_hourglass(arr, {'x': x, 'y': y})
            if new_val > maximum:
                maximum = new_val

    return maximum

def re_check_sum(arr, coords={'x': 0, 'y': 0}):

    maximum = sum_hourglass(arr, coords)

    if coords['y'] == 3:


def sum_hourglass(arr, coords):
# given x 

# and y coords, as well as an arr
# calculate 
    x = coords['x']
    y = coords['y']

    top = arr[y][x] + arr[y][x+1] + arr[y][x + 2]
    mid = arr[y + 1][x + 1]
    bottom = arr[y + 2][x] + arr[y + 2][x + 1] + arr[y + 2][x + 2]

    return top + mid + bottom

num_m = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

print(hourglassSum(num_m))