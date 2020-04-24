from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # Keeps track of the maximum number of nodes available to hold
        self.current = None # Stores the current position in the list
        self.storage = DoublyLinkedList() # DLL that holds values in a list

    def append(self, item):
        # If our list is below maximum capacity
        if self.storage.length < self.capacity:
            # Add the item to the tail end of the list
            self.storage.add_to_tail(item)
            # Set our current value to the head in the list
            self.current = self.storage.head
            
        # Otherwise, if our list is greater than or equal to maximum capacity
        elif len(self.storage) >= self.capacity:
            # Change the value of the oldest element to the new item coming in
            self.current.value = item

            # If the current oldest item is the tail, change it to the head
            if self.current == self.storage.tail:
                self.current = self.storage.head
                # Otherwise, make it the next node in the list
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        #Declare the current (starting) node as the head
        current = self.storage.head
        #While a current node exists (beginning with the head)
        while current:
            # Add the value of the head to the list
            list_buffer_contents.append(current.value)
            # Move the pointer over one to the right and run again until no more nodes
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


# ----------------TESTING-------------------


buffer = RingBuffer(3)

print(f'Initial Empty Array:', buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(f'First Pass:', buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(f'Overwrite Head:', buffer.get())  # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(f'Overwrite Mid and Last:', buffer.get())   # should return ['d', 'e', 'f']