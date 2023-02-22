def divide_plane(cord1,cord2,cord3,cord4):
    x1,y1=cord1
    x3,y1=cord4
    x3,y3=cord3
    x1,y3=cord2
    #find midpoint coordinates of the plane
    x_mid=(x1+x3)/2
    y_mid=(y1+y3)/2
    #create list of coordinates of square
    sq_1=[(x1,y1),(x_mid,y1),(x_mid,y_mid),(x1,y_mid)]
    sq_2=[(x_mid,y1),(x1,y3),(x3,y_mid),(x_mid,y_mid)]
    sq_3=[(x_mid,y_mid),(x3,y_mid),(x3,y3),(x_mid,y3)]
    sq_4=[(x1,y_mid),(x_mid,y_mid),(x_mid,y3),(x3,y1)]
    print("sq_1",sq_1)
    print("sq_2",sq_2)
    print("sq_3",sq_3)
    print("sq_4",sq_4)
divide_plane((0,0),(0,32),(32,32),(32,0))




