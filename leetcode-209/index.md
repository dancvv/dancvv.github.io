# [LeetCode 209] 长度最小的子数组


LeetCode 537，[题目链接点我](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)

这个题一开始想到了暴力破解的方式，利用两层for循环，以第一层为起点，在第二层里面不断累加，如果和大于等于target，记录当前长度，并与之前的长度做对比，然后结束第二层循环。不断的进行此操作就可以拿到结果。

代码如下：   
```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        // 暴力破解
        int res = Integer.MAX_VALUE;
        for(int i=0; i<nums.length; i++){
            int sum = 0;
            for(int j=i; j<nums.length; j++){
                sum += nums[j];
                if(sum >= target){
                    int subLen = j-i+1;
                    res = res > subLen ? subLen : res;
                    break;
                }
            }
        }
        // 此处判断结果是否变过
        return res == Integer.MAX_VALUE ? 0 : res;
    }
}
```
