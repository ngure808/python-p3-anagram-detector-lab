# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words_list):
        sorted_word = sorted(self.word)
        
        anagrams = []
        
        for word in words_list:
            if sorted(word) == sorted_word:
                anagrams.append(word)
        
        return anagrams