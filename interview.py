# #input 2 integer
# # concat
# 12, 345 ->12345, 34512
#
#
# 0 23 --> 23 , 230
# -21, -345 -> -21-345, -345-21 ->"can not concatenate"
#
# 23 , 32
# # input : 2 integer
# # output: integer


def concat(a, b):
    res1 , res2 = 0, 0
    # positive
    if a > 0 and b > 0:
        a_str = str(a)
        b_str = str(b)
        res1 = int(a_str + b_str)
        res2 = int(b_str + a_str)

    elif a == 0 and b == 0:
        return 0, 0
    # 0


    elif a == 0 or b == 0:
        if a == 0:  # 0, -123  ->123,  1230
            if b > 0:
                res2 = b

            res1 = b*10
            res2 = "None"
        else:
            res1 = a*10
            res2 = "None"




    # negative
    else:
        if a < 0 and b < 0:
            return "None"
        if a < 0:
            # a = -12, b = 34 ----> -1234, 34-12
            res1 = int(str(a) + str(b))
            res2 = "None"
        else:
            res1 = int(str(b)+str(a))
            res2 = "None"

    return res1, res2

a = 0
b = 1


# --> -10 an none
print(concat(a, b))




--------------------
import pandas as pd
full_path

name =
"".join(full_path + name)

1) open file  open_cvs
2) [:10]












