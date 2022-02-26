# [LeetCode 1523] 在区间范围内统计奇数数目


LeetCode 1523，[题目链接点我](https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range/)

一行代码解决

high加一是为了补上缺失的那一个，[0,x]范围的奇数必定为x的一半。如果x为奇数，比如7，根据Java的规则只能拿到3，实际有4个，就是把7给漏了，所以要加1.

代码如下：

```java
class Solution {
    public int countOdds(int low, int high) {
        return (high+1)/2 - low/2;
    }
}
```
