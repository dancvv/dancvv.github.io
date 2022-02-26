# [LeetCode 1706] 球会落何处


LeetCode 1706，[题目链接点我](https://leetcode-cn.com/problems/where-will-the-ball-fall/)

拿到这个题之后，首先分析其限制条件。根据题意可以发现，球会在三个地方卡住，左右两侧的墙壁上，以及两侧挡板形成的V型槽。

得到限制条件后，开始想怎么让程序找到路线，采用重力模拟的方法来实现。小球自上而下坠落，箱子已经按照二维数组的方式进行编码，那我们首先查第一列的小球，看它会不会成功走出小盒。也就是说采用两层for循环查找，第一层for循环用来演示每一列小球的位置，第二层for循环用来检验这一列小球会不会走出小盒。

在第二层for循环里，我们需要判断这个小球是否满足走出去的条件，即开始分析的三个地方。这里的难点在于不太好分析为什么不会再V型槽处卡住，小球卡住的V型槽都在同一层。那么只需要记录当前小球的移动位置，小球在下一层的坐标，把这个坐标带到当前层来，两个方向不一致就会在同一层形成V型槽，就卡住了。

代码如下：

```java
class Solution {
    public int[] findBall(int[][] grid) {
        int n = grid[0].length;
        int[] result = new int[n];
        for(int i=0 ; i<n ; i++){
            int col = i;
            for(int[] nums:grid){
                // 获取当前列的方向
                int direction = nums[col];
                // 移动后小球可能在的位置，左移一个，右移一个
                col += direction;
                // 判断小球在不在界内，col为小球移动后的坐标
                // 移动后的方向要求与上一个方向保持一致,一致就会形成V型槽
                if(col<0 || col==n || nums[col] != direction){
                    col = -1;
                    break;
                }
            }
            // 记录结果
            result[i] = col;
        }
        return result;
    }
}
```

