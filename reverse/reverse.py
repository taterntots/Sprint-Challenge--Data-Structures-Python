class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):

        # # Define our starting node and previous node
        # curr_node = self.head
        # prev = None

        # # (base case) If the list does not have any elements, OR
        # # (base case) If the list has only one element, return
        # if self.head == None or self.head.get_next() == None:
        #     return
        # # (base case) If there is no next element for our curr_node, make curr_node our header
        # if curr_node.get_next() == None:
        #     self.head = curr_node
        #     return

        # # Otherwise, recursively reverse the list
        # reverse_list(curr_node.get_next())
        # curr_node.get_next().set_next(curr_node)
        # curr_node.set_next(None)


        # ---------- Non-Recursive Solution -----------

        # (base case) If the list does not have any elements, OR
        # (base case) If the list has only one element, return
        if self.head == None or self.head.get_next() == None:
            return
        
        # Otherwise, run the code for reversing the list
        else:
            # Define our starting node and previous node
            curr_node = self.head
            prev_node = None

            # Loop through the list until there is no curr_node
            while curr_node:
                # Set the next_node to our get_next function
                next_node = curr_node.get_next()
                # Set the next node from our current node to the previous node
                curr_node.set_next(prev_node)
                # Redefine curr_node and prev_node
                prev_node = curr_node
                curr_node = next_node

            # If prev_node exists
            if prev_node:
                # Assign the head to the prev_node and return the prev_node
                self.head = prev_node
                return prev_node

n = Node(10, 20)

print(n.next_node)

l = LinkedList()

print(l.head)
l.add_to_head(1)
l.add_to_head(2)
l.add_to_head(3)
# l.reverse_list()

print(l)