# [LeetCode 537] 复数乘法


LeetCode 537，[题目链接点我](https://leetcode-cn.com/problems/complex-number-multiplication/)

这个题涉及到数学中复变函数的运算，也很简单，没有涉及到复杂运算，仅实现复数乘法。它的难处在于如何让两个字符串实现乘法运算。

简单科普一下复数乘法，两个复数的和依然是复数，它的实部是原来两个复数实部的和，它的虚部是原来两个虚部的和。复数的加法满足交换律和结合律。

根据复数乘法的规则，我们首先需要取到实部和虚部，这个可利用String类的split()方法，把一个代表复数的字符串分解为实部和虚部的字符数组。得到转换后的字符数组，我们将每个字符转换为整数，根据复数规则，进行分解运算。

分解运算具体步骤：
$(a+bi)*(c+di)=(a*c-b*d)+(a*d+b*c)i$

把分解运算的结果按照指定的字符串形式返回，代码如下：
```java
class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        String[] ss1 = num1.split("\\+|i"), ss2 = num2.split("\\+|i");
        int a = parse(ss1[0]), b = parse(ss1[1]);
        int c = parse(ss2[0]), d = parse(ss2[1]);
        int A = a * c - b * d, B = b * c + a * d;
        return A + "+" + B + "i";
    }
    int parse(String s) {
        return Integer.parseInt(s);
    }
}
```
