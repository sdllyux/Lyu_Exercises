"""
单词拆分
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
["cats and dog","cat sand dog"]

"""
class Solution:
    def wordBreak(self, s, wordDict):
        tmp = set("".join(wordDict))
        # [i not in tmp for i in s]为列表生成式简写
        # 列表生成式如下：     
        # list1 = []
        # for i in s:
        #     list1.append(i not in tmp)      
        if any([i not in tmp for i in s]):
            return []
        dp = [[""], [s[0]]*(s[0] in wordDict)]
        for i in range(1, len(s)):
            dp.append(sum([[f"{k} {s[j: i+1]}" if k else s[j: i+1] for k in dp[j]] for j in range(i+1) if s[j: i+1] in wordDict and dp[j]], []))
        return dp[-1]
