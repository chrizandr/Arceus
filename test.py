import pdb# Definition for singly-linked list.

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_end = False
        root_node = ListNode()
        final_list = root_node

        while(not all_end):
            flag = False
            min_val = -1 * float("inf")
            min_index = -1
            for i, l in enumerate(lists):
                if l is not None:
                    flag = True
                else:
                    continue
                if l.val > min_val:
                    min_index = i

            if not flag:
                all_end = True
                break

            new_node = ListNode(lists[min_index].val)
            lists[min_index] = lists[min_index].next
            final_list.next = new_node
            final_list = final_list.next

        return root_node.next


# 1 -> 4 -> 5
# 1 -> 3 -> 4
# 2 -> 6

def print_list(node_list):
    pass

nodes = []
l = [[1,4,5],[1,3,4],[2,6]]
for list in l:
    node = ListNode(list[0])
    for val in list[1::]:
        node.next = ListNode(val)
    nodes.append(node)

solution = Solution()
ndoe = solution.mergeKLists(nodes)
