class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        hash_map = {}

        for i in range(len(order)):
            hash_map[order[i]]=i

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if hash_map[word1[j]] < hash_map[word2[j]]:
                    break  # word1 is correctly before word2
                elif hash_map[word1[j]] > hash_map[word2[j]]:
                    return False  # word1 should come after word2 but appears before
            else:
                # If word1 is a prefix of word2, it must be shorter
                if len(word1) > len(word2):
                    return False   

        return True           
             

        