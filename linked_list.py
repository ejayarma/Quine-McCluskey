from node import Node
class LinkedList():
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def find (self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def add (self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def remove (self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None: # data is not in root node
                    prev_node.next_node = this_node.next_node
                else: # data is in root node
                    self.root = this_node.next_node
                self.size -= 1
                return True # data removed
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False # data not found

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end = '->')
            this_node = this_node.next_node
        print('None')