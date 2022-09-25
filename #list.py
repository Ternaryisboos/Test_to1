# #list
# from multiprocessing.sharedctypes import Value
# from tkinter import Y


# L =['lichael','Sarah','Tracy','bob','jack']

# print(L[0])
# print(L[1])
# print(L[2])


# r  = []
# n = 3
# for i in range(n):
#     r.append(i)


# print(r)
# print('===============')
# #Slicer
# print(L[0:3])

# #chuanjianshuju 

# L = list(range(100))
# #print(L)


# #L>>10
# print(L[::10])


# for i, values in enumerate(['a','b','c']):
#     print(i,values)


# # a = list(range(1,100))
# # print(a)


# print('===============')
# #xunhuan

# L = []
# for x in range(1,11): 
#     L.append(x * x)

# print(L)



# print('============')

# d = {'x': 'A', 'y': 'B', 'z': 'C' }

# print([k +'='+v for k,v in d.items()])


# B = [x for x in range(1,11) if x % 2 == 1 ]
# print(B)



#isinstance
# y = 'abc'
# w = 123
# print(isinstance(y,str))
# print(isinstance(w,str))



L1 = ['Hello','word',123,"pass"]
L2 = [L2.lower() for L2 in L1 if isinstance(L2,str)]

print(L2)









