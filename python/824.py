from typing import List


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        sentence2 = sentence.split(" ")
        res: List[str] = []
        for index, word in enumerate(sentence2):
            counter = index + 1
            latin_word = ""
            if word[0] in vowels:
                latin_word = word + "ma"
            else:
                latin_word = word[1:] + word[0] + "ma"
            while counter != 0:
                latin_word += "a"
                counter -= 1
            res.append(latin_word)
        return " ".join(res)


sol = Solution()
print(sol.toGoatLatin("I speak Goat Latin"))
