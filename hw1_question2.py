def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    def int_to_list(num):
        '''receivess an integer as an input. 
        Returns a list where each digit of the input number 
        is a value in the list. 
        '''
        lst=[]
        while num>0:
            lst.append(num%10)
            num//=10
        lst.reverse()
        return lst

    def is_palindrome(lst):
        n=len(lst)
        for i in range(n//2):
            if lst[i]!=lst[n-i-1]:
                return False
        return True

    for i in range(100000,1000000):
        n=len(int_to_list(i))
        if is_palindrome(int_to_list(i)[n-4::]):
            if is_palindrome(int_to_list(i+1)[n-5::]):
                if is_palindrome(int_to_list(i+2)[(n//2)-2:(n//2)+2]):
                    if is_palindrome(int_to_list(i+3)):
                        print(i)


if __name__ == '__main__':
    # Question 2
    check_palindrome()