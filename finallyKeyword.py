def access():
    try:
        l1=[1,2,3,4,5,6,7,8,9]
        i = int(input("enter the no to iterate: "))
        for i in l1:
            print(l1[i])
            # return 1


    except Exception as e:
        print(e)
        # return 0
    
    finally:
        print('This will be printed irrespective of the function returns to try or expect')
        
v= access()
print(v)
