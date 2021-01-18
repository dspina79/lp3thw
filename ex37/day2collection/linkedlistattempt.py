# Linked Lists?

class LinkedListElement(object):
    content = ""
    left = None
    right = None

    def __init__(self, content):
        super().__init__()
        self.content = content

    def print_left(self):
        if self.left:
            print(self.left.content)
        else:
            print("Left/parent is empty.")

    def print_right(self):
        if self.right:
            print(self.right.content)
        else:
            print("Right/child is emtpty.")

    def set_left(self, element):
        if self.left:
            self.left.right = element
        self.left = element
        self.left.right = self
    
    def set_right(self, element):
        if self.right:
            self.right.left = element
        self.right = element
        self.right.left = self

    def print_descentants(self):
        current_node = self
        while current_node:
            print(f"Current Node Contents: {current_node.content}")
            current_node = current_node.right



node_a = LinkedListElement("Content of A")
node_b = LinkedListElement("Content of B")
node_c = LinkedListElement("Content of C")
node_d = LinkedListElement("Content of D")
node_e = LinkedListElement("Content of E")

# make it so that the linking is e -> a -> d -> b -> c

print("Initializing Linked List")
node_e.set_right(node_a)
node_a.set_right(node_d)
node_d.set_right(node_b)
node_b.set_right(node_c)

node_e.print_descentants()

print("Now adding node X and Y to the middle.")
node_x = LinkedListElement("The Sly Node X!")
node_y = LinkedListElement("The Elusive Node Y")

node_a.set_left(node_x)
node_c.set_right(node_y)

node_e.print_descentants()