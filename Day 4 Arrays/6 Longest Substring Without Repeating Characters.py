#Given a string s, find the length of the longest substring without repeating characters.
#
# 
#
#Example 1:
#
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:
#
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:
#
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i , j = 0, 0
        max_len = 0
        curr_len = 0
        wordset = set()
        while j < len(s):
            if s[j] not in wordset:
                wordset.add(s[j])
                j += 1
            else:
                wordset = set()
                curr_len = j - i
                max_len = max(max_len, curr_len)
                i += 1
                j = i
        #if the longest unique formed till the last char in s
        curr_len = j - i
        max_len = max(max_len, curr_len)
        return max_len

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # create a window with left and right
        # keep a hash of elements already added
        left = 0
        right = 0
        seen = {} # keeps track of seen elements

        max_count = 0

        for i, character in enumerate(s):
            if character not in seen or seen[character] < left: # notice this logic
                seen[character] = i
                right = i
                if (right - left + 1) > max_count: # update the largest count
                    max_count = (right - left + 1)
            else:
                # we move start to one element after we found the character
                left = seen[character] + 1
                seen[character] = i # update index of last time we saw the character

        return max_count

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stk=[]
        maxLen=0
        for i in s:
            #Example aba
            #if stack is empty or char not in stack, append to stack
            if len(stk)==0 or i not in stk:
                stk.append(i)
            #Current Stack = [a,b]  
            elif i in stk:
                #Now i=a
                while i in stk:
                    #Current Stack(1) -> [b], a is not more in stack
                    stk.pop(0)
                #Append a to stack
                #Re calculate the maxLen
                stk.append(i)
            maxLen=max(maxLen,len(stk))
        return maxLen