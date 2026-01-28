class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for sign in ['!', '?', '\'', ',', ';', '.']:
            paragraph = paragraph.replace(sign, ' ')
        words = paragraph.lower().split()
        counter = Counter(words)
        sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        for word in sorted_counter:
            if word[0] in banned:
                continue
            return word[0]
