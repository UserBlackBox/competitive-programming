// https://binarysearch.com/problems/Length-of-a-Linked-List

class Solution {
    solve(node) {
        if(node == null) return 0;
        let len = 1;
        while(node.next!=null){
            len += 1;
            node = node.next;
        }
        return len;
    }
}
