# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    the_word = word.replace("","").lower()
    anag = anagram.replace("","").lower()

    if (len(the_word) == len(anag)):

        sorted_word_1 = sorted(the_word)
        sorted_word_2 = sorted(anag)

        if (sorted_word_1== sorted_word_2):
         print("True")
        else:
            print("false")
    else:
        print("Input not valid")
find_anagram("hello","world")
find_anagram("bite","biet")

