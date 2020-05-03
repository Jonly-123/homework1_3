# row=行   
# col=列

# 左下角三角形
def left_down_triangle():
    for row in range(1,10):
        for col in range(1,row+1):
            print('{}*{}={:<4}'.format(row,col,row*col),end=' ')
        print('')



# 左上角三角形
def left_up_triangle():
    for row in range(9,0,-1):
        for col in range(1,row+1):
            print('{}*{}={:<4}'.format(row,col,row*col),end=' ')
        print('')

 

# 右下角三角形
def right_down_triangle():
    for row in range(1,10):
        for i in range(1,10-row):
            print(end='         ')
        for col in range(row,0,-1):
            print('{}*{}={:<4}'.format(row,col,row*col),end=' ')
        print('')


#右上角三角形
def right_up_triangle():
    for row in range(9,0,-1): #打印行
        for i in range(9,row,-1):
            print(end='         ')
        for col in range(row,0,-1): #打印列
            print('{}*{}={:<4}'.format(row,col,row*col),end=' ')
        print(' ')




print('='*90)
left_down_triangle()
print('='*90)
left_up_triangle()
print('='*90)
right_down_triangle()
print('='*90)
right_up_triangle()
print('='*90)

















# for row in range(9,0,-1):
#     col=9
#     while col>=row:
#          print('{}*{}={:<4}' .format (row, col, row*col), end=' ')
#          col-=1
#     print("")

