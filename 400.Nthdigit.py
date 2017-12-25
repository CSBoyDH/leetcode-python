# 给定一个无穷整数序列1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 求序列的第n位数字。
#
# 注意：
#
# n是正数并且范围在32位带符号整数之内（n < 2^31）
# 将整数序列划分为下列区间：
#
# 1   1-9
# 2   10-99
# 3   100-999
# 4   1000-9999
# 5   10000-99999
# 6   100000-999999
# 7   1000000-9999999
# 8   10000000-99999999
# 9   100000000-99999999
# 然后分区间求值即可。
# 分析可以得出一位有９个数字，二位数有90个数字，三位数有900个数，依次类推．
# 因此可以每次增加一位数字，看n是否还在这个范围内．例如给定n = 150，首先一位有９个数字，
# 所以位数可以＋１，这样n-9 = 141. 然后２位的数字有２＊９０= 180，大于１４１，所以目标数字肯定是２位的．
# 然后求具体落在哪个数字．可以用10+(141-1)/2 = 80求出．再求具体落在哪一位上，
# 可以用(141-1)%2＝０求出为第０位，即８．如此即可．
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(9):
            d = 9 * 10 ** i
            if n <= d * (i + 1): break
            n -= d * (i + 1)
        n -= 1
        return int(str(10**i + n / (i + 1))[n % (i + 1)])
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        count=10**i-10**(i-1)
        #print count
        while(n-count>0):
            n=n-count
            i+=1
            count=(10**i-10**(i-1))*i
        mod=n%i
        if(mod==0):
            ans=str(10**(i-1)-1+n/i)
            return int(ans[-1])
        else:
            ans=str(10**(i-1)+n/i)
            return int(ans[mod-1])