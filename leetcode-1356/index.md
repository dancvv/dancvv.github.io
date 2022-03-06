# [Leetcode 1356] 统计数字在二进制下1的数目排序


LeetCode 1356，[题目链接](https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/)

代码如下：

```java
class Solution {
    public int[] sortByBits(int[] arr) {
        // 巧妙的解法
        // 利用java自身携带的统计函数
        for(int i=0; i<arr.length; i++){
            arr[i] = Integer.bitCount(arr[i]) * 1000000 + arr[i];
        }
        Arrays.sort(arr);
        // 排序完之后对数组进行取余操作，得到原来的数组
        for(int i=0; i<arr.length; i++){
            arr[i] = arr[i] % 1000000;
        }
        return arr;
    }
}
```

