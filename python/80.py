from typing import Dict, List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_alphabet: Dict[str, str] = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }
        morse_words: List[str] = []
        for word in words:
            string = ""
            for char in word:
                string += morse_alphabet[char]
            morse_words.append(string)
        return len(set(morse_words))


sol = Solution()
print(sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
