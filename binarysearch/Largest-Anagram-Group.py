# https://binarysearch.com/problems/Largest-Anagram-Group

class Solution:
    def solve(self, words):
        anagrams = {}
        for i in range(len(words)):
            words[i] = "".join(sorted(list(words[i])))
            if words[i] in anagrams:
                anagrams[words[i]]+=1
            else:
                anagrams[words[i]]=1
        return max(anagrams.values())

