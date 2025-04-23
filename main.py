from dataclasses import dataclass
import unittest

@dataclass
class Node:
    value: int
    next: 'Node' = None


class LinkedList:
    def insert_back(self, value):
        if not hasattr(self, 'head') or self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def get_head(self):
        return getattr(self, 'head', None)


class Ll:
    def add(self, l1: LinkedList, l2: LinkedList) -> LinkedList:
        result = LinkedList()
        carry = 0
        n1 = l1.get_head()
        n2 = l2.get_head()

        while n1 or n2 or carry:
            val1 = n1.value if n1 else 0
            val2 = n2.value if n2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            result.insert_back(total % 10)

            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next

        return result


class TestLl(unittest.TestCase):
    def setUp(self):
        self.ll = Ll()

    def create_list(self, values):
        l = LinkedList()
        for v in values:
            l.insert_back(v)
        return l

    def assertLinkedListEqual(self, head, expected):
        current = head
        for val in expected:
            self.assertIsNotNone(current, "Too short")
            self.assertEqual(current.value, val)
            current = current.next
        self.assertIsNone(current, "Too long")

    def test_1(self):
        # 341 + 789 = 1130 → [0, 3, 1, 1]
        l1 = self.create_list([1, 4, 3])
        l2 = self.create_list([9, 8, 7])
        result = self.ll.add(l1, l2)
        self.assertLinkedListEqual(result.get_head(), [0, 3, 1, 1])

    def test_2(self):
        # 9999 + 1 = 10000 → [0, 0, 0, 0, 1]
        l1 = self.create_list([9, 9, 9, 9])
        l2 = self.create_list([1])
        result = self.ll.add(l1, l2)
        self.assertLinkedListEqual(result.get_head(), [0, 0, 0, 0, 1])

    def test_3(self):
        # 81 + 35 = 116 → [6, 1, 1]
        l1 = self.create_list([1, 8])
        l2 = self.create_list([5, 3])
        result = self.ll.add(l1, l2)
        self.assertLinkedListEqual(result.get_head(), [6, 1, 1])

    def test_4(self):
        # 0 + 7 = 7 → [7]
        l1 = self.create_list([0])
        l2 = self.create_list([7])
        result = self.ll.add(l1, l2)
        self.assertLinkedListEqual(result.get_head(), [7])

    def test_5(self):
        # 29 + 38 = 67 → [7, 6]
        l1 = self.create_list([9, 2])
        l2 = self.create_list([8, 3])
        result = self.ll.add(l1, l2)
        self.assertLinkedListEqual(result.get_head(), [7, 6])


if __name__ == "__main__":
    unittest.main()


