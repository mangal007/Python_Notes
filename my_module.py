def palindrome(strng):
    '''To check if a sting is palindrome'''
    if (strng[::-1] == strng):
        return "String is a palindrome"
    else:
        return "string is not a palindrome"
        
def fact(num):
    '''Program for factorial'''
    if(num == 0):
        return 1
    else:
        return num * fact(num-1)

#print(__name__)      # it's out come here is __main__ but when this file is imported in other name than it come by its name which is my_module

#for testing purpose we line below code. In project this file will be imported and we will be using these functions. so for testing we just #need one argument which we given below by adding a condition so that it can be used in testing only

if __name__ == '__main__':
    print(palindrome('level'))
    print(fact(5))