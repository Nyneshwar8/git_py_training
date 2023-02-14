a = 40
def outer():
    a = 10

    def inner():
        nonlocal a         #there are local and non local
        print('2: ',a)

        a = 20
        def one_more_inner():
           print("4:",a)

        one_more_inner()    #this is the call
        print("3:",a)


    inner()
    print('5 : ',a )


print("1 :",a)
outer()
print("6 : ",a)
