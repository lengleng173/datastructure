# 给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。

#  s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。

# 例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
# 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。

# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
# 子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
# 子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
# 输出顺序无关紧要。返回 [9,0] 也是可以的。

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        a=dict()
        for i in words:
            a[i]=a.get(i,0)+1
        n=len(words[0])
        re=[]
        l,r,maxlen=0,n,n*len(words)
        if n==len(s) and len(words)==1:
            if s==words[0]:
                return [0]
            else:
                return []
        while r<len(s):
            start=l
            b=a.copy()
            while s[l:r] in b and b[s[l:r]]>0:
                if r-start==maxlen:
                    re.append(start)
                    break
                b[s[l:r]]=b[s[l:r]]-1
                l+=n
                r+=n
            l=start+1
            r=l+n
        return re
    
so=Solution()
s = "a"
words = ["a"]
print(so.findSubstring(s,words))

# from collections import Counter

# class Solution(object):
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         if not s or not words:
#             return []
        
#         word_len = len(words[0])
#         total_len = word_len * len(words)
#         word_count = Counter(words)
#         result = []
        
#         # 只需要遍历word_len个不同的起始偏移
#         for i in range(word_len):
#             left = i
#             right = i
#             current_count = Counter()
#             words_found = 0
            
#             while right + word_len <= len(s):
#                 word = s[right:right + word_len]
#                 right += word_len
                
#                 if word in word_count:
#                     current_count[word] += 1
#                     words_found += 1
                    
#                     # 如果某个单词出现次数过多，移动左边界
#                     while current_count[word] > word_count[word]:
#                         left_word = s[left:left + word_len]
#                         current_count[left_word] -= 1
#                         words_found -= 1
#                         left += word_len
                    
#                     # 如果找到了所有单词
#                     if words_found == len(words):
#                         result.append(left)
#                         # 移动左边界，继续寻找
#                         left_word = s[left:left + word_len]
#                         current_count[left_word] -= 1
#                         words_found -= 1
#                         left += word_len
#                 else:
#                     # 如果遇到不在words中的单词，重置窗口
#                     current_count.clear()
#                     words_found = 0
#                     left = right
        
#         return result