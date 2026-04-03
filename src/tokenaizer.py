import dataclasses
import random

class Tokenaizer:
    def __init__(self, file_path: str):
        self.path = file_path
        self.words_matrix = []
        self.unique_words = set()
        self.int_matrix = []

    def _check_unique_and_add_word(self, curr_word: list, ans: list):
        new_word = "".join(curr_word)
        ans.append(new_word)
        self.unique_words.add(new_word)
        curr_word.clear()

    def tokenaize_sentence(self, sentence: str):
        curr_word = []
        ans = []
        
        for char in sentence:
            if char == " ":
                if curr_word:
                    self._check_unique_and_add_word(curr_word, ans)
            
            elif not char.isalnum():
                if curr_word:
                    self._check_unique_and_add_word(curr_word, ans)
                
                if char != '\n' and char != '\r':
                    self.unique_words.add(char)
                    ans.append(char)
            
            else:
                curr_word.append(char)

        if curr_word:
            last_word = "".join(curr_word)
            ans.append(last_word)
            self.unique_words.add(last_word) 
                
        return ans
    
    def build_words_matrix(self):
        ans = []
        with open(self.path, "r") as file:
            self.words_matrix = [self.tokenaize_sentence(sentence) for sentence in file]

        
    def build_dictionary(self):
        word_int_map = {word: index for index, word in enumerate(self.unique_words)}
        
        for sentence in self.words_matrix:
            new_int_list = []
            for word in sentence:
                int_equivalent = word_int_map.get(word)
                new_int_list.append(int_equivalent)
                
            self.int_matrix.append(new_int_list)


    def no_idea(self, ):
        
        V = len(self.unique_words)
        D = 100
        matrix = [[random.uniform(-0.5, 0.5) for _ in range(D)] for _ in range(V)]
        

    
