// Title: Add Two Numbers
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/add-two-numbers/

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, sum_val = divmod(val1 + val2 + carry, 10)
            curr.next = ListNode(sum_val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        while l1 or l2 or carry:
        carry = 0
        curr = dummy_head
        dummy_head = ListNode(0)
        return dummy_head.next
