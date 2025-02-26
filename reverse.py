class reverse:
    def __init__(self, word):
        self.word= word
        
    def reverse_word(self):

        return self.word[::-1]
    

original_word = input("Enter the word you want reversed : ")
rev = reverse(original_word)

print(f"The word {original_word} reversed is {rev.reverse_word()}")