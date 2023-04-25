furry=True
large=True
if furry:
    if large:
        print("furry_True,Large_True")
    else :
        print("furry_True,Large_False")
else :
    if large:
        print("furry_False,Large_True")
    else :
        print("furry_False,Large_False")
print("=================================")
if furry & large:
    print("furry_True,Large_True")
elif furry==True & large==False:
    print("furry_True,Large_False")
elif furry==False & large==True:
    print("furry_False,Large_True")
elif furry==False & large==False:
    print("furry_False,Large_False")
