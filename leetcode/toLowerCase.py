# 'A' - 'Z' 对应的 ascii 是 65 - 90；
# 'a' - 'z' 对应的 ascii 是 97 - 122；
class Solution:
    def toLowerCase(self, str):
        s = []
        for i in str:
            # 根据ascii码来判断大小写字母
            if 65 <= ord(i) <= 90:
                # 通过把ascii码增加32来把大写字母变成小写字母
                s.append(chr(ord(i) + 32))
            else:
                s.append(i)
        print(''.join(s))

sl = Solution()
sl.toLowerCase('Hello')
