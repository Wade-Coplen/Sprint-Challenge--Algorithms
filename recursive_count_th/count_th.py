'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
----------------
Understand:
- find the number of --th's-- in 'word'
- case matters. How do we specify lower case in python
- has to use recursion.
- we need to iterate over the words and find 'th' in each word
- what is the recursive case
- what is base case
'''
def count_th(word):
    #print(word)
    value = "th"
    print(value)
    count = 0
    if value not in word:
        return count
    else:
        return count_th(word[1:]) +1
        
            #print('There are {count}'.format(word))

    
   
    # TBC

    

