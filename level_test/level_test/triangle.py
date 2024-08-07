def triangle(n):
    width = 4 * 2**(n-1)
    half_of_width = 2*2**(n-1)
    print(' ' * (half_of_width-1) + '*')

    for j in range (1,(half_of_width)-1):
        j_remainder = j % 4
        print(' ' * (half_of_width - 2*j) + '*' + ' '*(2*j-1) + '*')
    print(' '* (4*(n-1)-1) + '* ' * (half_of_width))
    for i in range ((half_of_width)+1, width -1):
        remainder = i % 4
        print(' ' * (width-i-2) + '*' + ' '* (2*remainder-1)+'*'+' '*(2**(n+1)-(width-i-2)-(2*remainder-1)-(2*remainder-1)-2) +'*'+' '*(2*remainder-1) + '*')
    print('* '* (width))