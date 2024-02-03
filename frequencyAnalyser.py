
alphabet = ['a', 'b','c','d','e','f', 'g', 'h', 'i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
common_frequency = 'etaoinshrdlucmfwypvbgkjqxz'

def construct_frequency_table(cypher):
    # constructs a frequency table from a cypher text
    # return the frequency table as a list of 26 numbers
    # according to the alphabet 
    lst = [0] * 26
    for c in cypher:
        if c.lower() in alphabet:
            lst[alphabet.index(c)] += 1
    return lst

def construct_key(frequency_table):
    key = [None] * 26
    for i in range(26):
        index = find_max_index(frequency_table)
        key[i] = alphabet[index]
        frequency_table[index] = -1
    return key

def decypher(cypher, key):
    text = str()
    for c in cypher:
        index = key.index(c)
        text += common_frequency[index]
    return text

def find_max_index(lst):
    # find the max value in a list of values.
    # return the first found index of the max value 
    index = 0
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
            index = i
    return index


#unit tests
assert construct_frequency_table('aaaabbbddf') ==  [4, 3, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert find_max_index([3, 7, 12, 5, 0]) == 2
assert construct_key([4, 3, 0, 2, 0, 1, 0, 5, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == ['k', 'h', 'a', 'b', 'd', 'f', 'c', 'e', 'g', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
assert decypher('aaaabbbddf', ['a', 'b', 'd', 'f', 'c', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 'eeeetttaao'