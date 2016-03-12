import math

def move_to(object, to_x, to_y):
    object.update()

    vector = math.sqrt(pow(to_x - object.winfo_x(), 2) + pow(to_y - object.winfo_y(), 2))
    X = (to_x - object.winfo_x()) / vector
    Y = (to_y - object.winfo_y()) / vector

    object.place(x=object.winfo_x()+X*8, y=object.winfo_y()+Y*8)

    if abs(to_x-object.winfo_x()) > 10 or abs(to_y-object.winfo_y()) > 10:
        object.after(5, move_to, object, to_x, to_y)
