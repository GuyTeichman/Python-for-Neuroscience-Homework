def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    flag=0
    skip=0
    for curr in range(len(word)-1):
        if word[curr+skip]==word[curr+skip+1]:
            flag+=1
            skip+=1
            if flag==3:
                return True
        else:
            flag=0
        if curr+skip+2>=len(word):
            return False
    return False

if __name__ == '__main__':
    # Question 1
    word_with_repeats='gtaabbcc6'
    #word_without_repeats='assdddvv'
    return_value = trifeca(word_with_repeats)
    print('Question 1 input: ',word_with_repeats)
    print(f"Question 1 solution: {return_value}")