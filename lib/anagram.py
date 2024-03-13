class Anagram:
    def __init__(self, word) -> None:
        self.word = word

    def match(self, match_list):
        result = []
        for word in match_list:
            if sorted(self.word) == sorted(word):
                result.append(word)
        return result