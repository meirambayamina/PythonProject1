class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Task 1: Add element to the beginning
    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Task 2: Add element to the end
    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Task 3: Remove the last element
    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    # Task 4: Print all elements
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Task 5: Search for a specific element
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Task 6: Insert element at a given position
    def insert_at_position(self, data, position):
        if position == 0:
            self.add_to_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current:
                current = current.next
        if current:
            new_node.next = current.next
            current.next = new_node

    # Task 7: Remove element by value
    def remove_by_value(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    # Task 8: Combine two linked lists
    def combine(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = other_list.head

    # Task 9: Reverse a linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Task 10: Sort a linked list (insertion sort)
    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, head_ref, new_node):
        if not head_ref or head_ref.data >= new_node.data:
            new_node.next = head_ref
            return new_node
        current = head_ref
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head_ref


list1 = LinkedList()

#task2
list1.add_to_end(10)
list1.add_to_end(20)

#task1
list1.add_to_beginning(5)

#task6
list1.insert_at_position(15, 2)

#task4
print("Список 1:")
list1.print_list()

#task5
print("Поиск 15:", list1.search(15))

#task3
list1.remove_last()
print("После удаления последнего:")
list1.print_list()

#task7
list1.remove_by_value(15)
print("После удаления значения 15:")
list1.print_list()

#create new list to combine in task 8
list2 = LinkedList()
list2.add_to_end(30)
list2.add_to_end(25)

#task8
list1.combine(list2)
print("После объединения:")
list1.print_list()

