# 小红穿越沼泽地


网易笔试题的最后一道，以前都不敢想，最后一道那指定是最难的，到题目的时候我哭了，怎么回事也没有想象中的难啊！到最后也没写完，遗憾离场。

题目复述，走沼泽，在一片m*n的沼泽地里，1代表沼泽，0代表平底，一开始的时候在左上角。从0到1和从1到0都需要花费2个单位时间，相同的地形只需要1个单位时间，小红只能向左、向右或者向下。请问经过这篇沼泽最少需要花费多少时间？

一看就是经典的动态规划问题，需要找到怎么用最少的时间通过沼泽地。首先确定一下小红能怎么走，根据题目，小红只能向右或者向下走，向左就是走回头路了，反而增加时间，不考虑。

确定走的路线了，那么现在的问题是小红怎么用最好的时间从上一个位置走到当前位置。我们可以先确定一下从上一个位置当当前位置需要花费的时间，如果地形相同则为1，否则为2，然后与上一个位置的路线总耗时相加，即dp[i-1][j] + route[i][j] == route[i-1][j] ? 1 : 2。后面的表达式代表上一位置与当前位置如果地形相同则花费时间为1，否则为2。

具体实现看代码吧：

```java
public class NetEase04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int[][] route = new int[m][n];
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                route[i][j] = sc.nextInt();
            }
        }
        int[][] dp = new int[m][n];
        for(int i=0;i<m; i++){
            for(int j=0; j<n; j++){
                if(i==0 && j==0){
                    dp[i][j] = 0;
                }else if(i == 0){
                    int temp = route[i][j-1] == route[i][j] ? 1 : 2;
                    dp[i][j] = dp[i][j-1] + temp;
                }else if(j == 0){
                    int temp = route[i-1][j] == route[i][j] ? 1 : 2;
                    dp[i][j] = dp[i-1][j] + temp;
                }else {
                    int x_1 = route[i-1][j] == route[i][j] ? 1 : 2;
                    int y_1 = route[i][j-1] == route[i][j] ? 1 : 2;
                    dp[i][j] = Math.min(dp[i-1][j]+x_1, dp[i][j-1]+y_1);
                }
            }
        }
        System.out.println(dp[m-1][n-1]);
    }
}
```
