class Solution(object):
    def maximum69Number (self, num):
        if not num:
            return 0
        # int转换为string再转换为list
        list_num = list(str(num))
        for i in range(len(list_num)):
            # 把碰到的第一个6换成9
            if list_num[i] == '6':
                list_num[i] = '9'
                break
        # list转换为str再转换为int
        return int("".join(list_num))