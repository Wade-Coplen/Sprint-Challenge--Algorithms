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
Must have a base case.
Must change its state to move towards the base case.
Must call itself.
'''
def count_th(word):
    string = word
    value = 't'
    v = value.lower()
    value2 = 'h'
    v2 = value2.lower()
    count = 0
    count2 = 0
    for i in word:
        for j in word:
            if i == v:
                count = count +1
                if j == v2:
                    count2 = count +1

                print('i am count 1', count)
                print('i am count 2', count2)
                print('total', count + count2)

  
    

    
        
            #print('There are {count}'.format(word))

    
   
    # TBC

    

