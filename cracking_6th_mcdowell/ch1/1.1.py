#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional date structures

def search(word):
    n=0
    for digit in range(0, len(word)+1):
        n+=1
        for i in range(n, len(word)):
            print([digit,i])
            if word[digit] == word[i]:
                return 'fail'
    return 'pass'

def main():
    word = 'hypermobile'
    print(search(word))
    
main()

### ----------------------------------------------- ###

word2 = 'hypermobile'
list_of_char = [word2[0]]
for index in range(1,len(word2)):
    if word2[index] in list_of_char:
        print('Dublicate found')
        break
    else:
        list_of_char.append(word2[index])

if len(list_of_char) == len(word2):
    print('all char unique')
            
        