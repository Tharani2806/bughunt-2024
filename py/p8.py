class doubly_linked_list(object):
    def _init_(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, data):
        # Append an item 
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

        self.count += 1

    def print_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

items = doubly_linked_list()
items.append_item('C#')
items.append_item('C++')
items.append_item('PHP')
items.append_item('Java')
items.append_item('Python')

print("Print Items in the Doubly linked:")
items.print_forward()
