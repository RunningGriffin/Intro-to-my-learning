# Given two Strings write a method to decide if one is a permutation of the other
def check_perm(parent_string,child_string):
    
    if len(parent_string) != len(child_string):
        return('Not a permutation')
    
    parent_dict = {}
    for letter in parent_string:
        if letter not in parent_dict:
            parent_dict[letter] = 1
        else:
            parent_dict[letter] += 1
        
    for letter in child_string:
        if letter in parent_dict:
            parent_dict[letter] -= 1
            if parent_dict[letter] == 0:
                parent_dict.pop(letter)
        else:
            return('Not a permutation')
    return('Is a permutation')
        
def main():
    parent_string = 'hyperbole'
    child_string = 'hlobrepyh'
    print(check_perm(parent_string,child_string))
    
main()

        