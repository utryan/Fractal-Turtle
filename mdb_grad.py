# Sea Blue Gradient for the Mandelbrot Set
clr_lst = ['#0645a4', '#154ba8', '#2052ac', '#2958b0', '#315fb5',
           '#3965b8', '#416bbc', '#4872c0', '#4f78c4', '#577fc8',
           '#5e85cb', '#658ccf', '#6d93d2', '#7499d6', '#7ca0d9',
           '#84a6dd', '#8bade0', '#93b4e4', '#9bbae7', '#a4c1ea',
           '#acc8ee', '#b4cef1', '#bdd5f4', '#c5dcf7', '#cee2fb',
           '#d7e9fe', '#cee2fb', '#c5dcf7', '#bdd5f4', '#b4cef1',
           '#acc8ee', '#a4c1ea', '#9bbae7', '#93b4e4', '#8bade0',
           '#84a6dd', '#7ca0d9', '#7499d6', '#6d93d2', '#658ccf',
           '#5e85cb', '#577fc8', '#4f78c4', '#4872c0', '#416bbc',
           '#3965b8', '#315fb5', '#2958b0', '#2052ac', '#154ba8']

# Function that outputs hex value given a complex parameter
def mcolor(comp_num, cycle):
    iter_num = complex(0,0)

    for clr_num in range(50 * cycle):
        iter_num = iter_num ** 2 + comp_num

        if abs(iter_num) >= 2:
            return clr_lst[clr_num % 50]
            # return '#FFFFFF'

    return '#000000'

# Same as above but for Julia Sets
def jcolor(comp_num, const, cycle):
    iter_num = comp_num

    for clr_num in range(50 * cycle):
        iter_num = iter_num ** 2 + const

        if abs(iter_num) >= 2:
            return clr_lst[clr_num % 50]
            # return '#FFFFFF'

    return '#000000'
