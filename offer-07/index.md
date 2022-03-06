# 面试题 02.07 链表相交

面试题 02.07 链表相交，[题目链接点我](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/)

这个题我先用了最耗时的方法做，既然是让最第一个相交的节点，也就是说，找到第一个相等的点。既然是相等，那么我把一个链表的所有节点存到一个哈希表中，让后让第二个链表在遍历的同时，不停确认哈希表中是不是有这个节点，如果有，终止循环，找到节点，没有就返回null。

代码如下：   
```java
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode cross = null;
        ListNode loopA = headA;
        ListNode loopB = headB;
        if(headA ==null || headB ==null) return cross;
        Map<ListNode,Integer> hash = new HashMap<>();
        while(loopA != null){
            hash.put(loopA,loopA.val);
            loopA = loopA.next;
        }
        while(loopB != null){
            if(hash.containsKey(loopB)){
                cross = loopB;
                // 条件符合之后需要跳出循环
                break;
            }
            loopB = loopB.next;
        }
        return cross;
    }
}
```

也有十分巧妙的解法，两个链表如果相交，遍历完a后，紧接着遍历b，另一个链表b采取同样的操作，遍历完b，然后遍历a，他们会在相等的位置停下。因为a+b=b+a，其长度一致，转一圈终究会回到共同的点。如果两个链表没有相交的点，A的长度是a，B的长度是b，如果两者不相交，则两链的头结点在同时走了a+b步后均会指向null，即满足了循环的终止条件。

代码如下：

```java
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA, b = headB;
        // A的长度是a，B的长度是b，如果两者不相交，则两链的头结点在同时走了a+b步后均会指向null，即满足了循环的终止条件。
        while(a != b){
            a = a != null ? a.next : headB;
            b = b != null ? b.next : headA;
        }
        return a;
    }
}
```
