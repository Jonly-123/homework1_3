# row 
# col

# 左下角三角形
def left_down_triangle():
    row = 1
    while row< 10:
        col = 1
        while col < row+1:
            print('{}*{}={:<4}'.format(row, col, row*col), end='')
            col += 1
        row += 1
        print("")

# 左上角三角形
def left_up_triangle():
    row = 1
    while row < 10:
        col = row
        while col < 10:
            print('{}*{}={:<4}' .format (row, col, row*col), end=' ')
            col += 1
        row += 1
        print("")


# 右下角三角形
def right_down_triangle():
    row = 1
    while row < 10:
        col = 1
        while col < 10-row:
            print(end='        ')
            col +=1
        while col <10 and col>=(10-row):
            print('{}*{}={:<4}'.format(row,col,row*col),end='')
            col +=1
        row +=1
        print('')


#右上角三角形

def right_up_triangle():
    row = 1
    while row <10:
        col = 1
        i = row
        while i > 1 and col < 10:
            print(end='        ')
            i -= 1
            col += 1
        while row <= col < 10:
            print('{}*{}={:<4}'.format(row,col,row*col),end='')
            col += 1
        row += 1
        print('')
    


print('='*90)
left_down_triangle()
print('='*90)
left_up_triangle()
print('='*90)
right_down_triangle()
print('='*90)
right_up_triangle()
print('='*90)


