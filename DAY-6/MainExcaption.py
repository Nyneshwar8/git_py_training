class Emp:

    def __init__(self,eid,enm):
        self.empId = eid
        self.empName = enm

e1 = Emp(101,"ABCD")
value = [1,2,3,4,5]
values = {1:100}
try:
    num1 = int(input('Enter Number 1 :'))           # valueerror
    num2 = int(input('Enter Number 2 : '))          #valueerror
    result = num1 / num2                            #zerodiv
    print(e1.empAge)                                #attribu
    print(value[5])                                 #indexerr
    print(values[2])                                #keyerror
    value[10] = 10/3
except KeyError:
    print('KeyError') # invalid key in dict
except ValueError:                                             #BaseException -- By default
    print('ValueError -- only digits required')
except IndexError:
    print('Index Error -- only allowed index 0-len-1')
except:
    print('BaseException..')
else:
    pass
finally:
    pass



print('Program executed normally....!')