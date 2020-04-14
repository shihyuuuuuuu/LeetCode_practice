class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabets = [chr(i) for i in range(97, 123)]
        words_morse = [""] * len(words)
        for index, word in enumerate(words):
            for c in word:
                words_morse[index] += morse[alphabets.index(c)]
        return len(set(words_morse))
