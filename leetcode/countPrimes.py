class Solution(object):
    def countPrimes(self, n):

        # 最小的质数是2
        if n < 2:
            return 0

        # 创建列表，记录质数个数，列表下标表示数字，列表值为1代表质数，0代表不是质数
        is_Primes = [1] * n
        # 排除0和1两个非质数
        is_Primes[0] = is_Primes[1] = 0

        for i in range(2, n):
            # 判断存在
            if is_Primes[i]:
                # 从i*i开始，每隔i个数截取一次列表并将对应值更新为0，((n - 1 - i*i) // i + 1)表示质数个数
                is_Primes[i*i: n: i] = [0] * ((n - 1 - i*i) // i + 1)
        print(sum(is_Primes))

        # 输出质数
        j_num = []
        for j in range(0,len(is_Primes)):
            if is_Primes[j] == 1:
                j_num.append(j)
        print(j_num)
sl = Solution()
sl.countPrimes(10)