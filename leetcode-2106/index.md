# [LeetCode 2106] 增量元素之间的最大差值


LeetCode 2106，题目链接：<https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements/>

这个题虽然是个简单题，但是我还是花了一点时间来解答，猛的想错了方向，差点没绕出来。其实，还是很简单的，只需要采用一个for循环外加两个条件判断即可。

在循环内，我们首先要知道这个数组的最小值，那么简单的if判断就能找到最小值。现在的问题怎么找到第二个数，使得两者之间的差值最大。题目要求第二个数必须在第一个数后面，也就是说两个数的序号必须是一前一后，前面的数小于后面的数。

思路有了，代码如下：
```java
class Solution {
    public int maximumDifference(int[] nums) {
        int diff = -1;
        int min = nums[0];
        for(int i=1;i<nums.length;i++){
            // 找到最小值
            if(min > nums[i]){
                min = nums[i];
            }else if(nums[i]>min){
                // 判断差值是否小于当前差值,同时，相减的两个数不能相等
                diff = Math.max(diff, nums[i] - min);
            }
        }
        return diff;
    }
}
```
