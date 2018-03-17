print("palindrome")
def palindrome(word):
    word = word.lower()
    return word[::-1] == word
print(palindrome("mother"))
print(palindrome("Mom"))


print("anagram")
def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()

    return sorted(w1) == sorted(w2)

print(anagram("iceman", "cinema"))
print(anagram("leef", "left"))


print("count_character")

def count_character(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)

count_character("Dynasty")

print("再起")

def bottles_of_beer(bob):
    """ prints Bottle of Beer on the wall lyrics.

    :
    param bob: Must be a positive Integer
    """
    if bob < 1:
        print("""No more bottles of beer on the wall.
            No more bottles of beer.

        """)
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall,
            {} bottles of beer.
            Take one down and pass it around,
            {} bottles of beer on the wall.

            """.format(tmp, tmp, bob))
    bottles_of_beer(bob)

bottles_of_beer(99)
