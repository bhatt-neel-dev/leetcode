// Title: Add Two Numbers
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/add-two-numbers/

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
        while l1 or l2 or carry:
            carry, sv = divmod(v1+v2+carry, 10)
            curr.next = ListNode(sv)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next
