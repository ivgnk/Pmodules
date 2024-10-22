# How to implement a binary tree?
# https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        print('\nfind - ',val)
        if self.root:
            return self._find(val, self.root)
        # print('\nfind - end')

    def _find(self, val, node):
        if val == node.val:
            return node
        elif val < node.val and node.left:
            return self._find(val, node.left)
        elif val > node.val and node.right:
            return self._find(val, node.right)

    def delete_tree(self):
        # garbage collector will do this for us.
        print('\ndelete_tree')
        if self.root:
            self.root = None

    def view_tree(self):
        print('\nview_tree - beg- ')
        if self.root:
            self._view_tree(self.root)
        print('\nview_tree - end- ')

    def _view_tree(self, node):
        if node:
            self._view_tree(node.left)
            print(node.val, end = " ")
            self._view_tree(node.right)
################
def the_in_test():
    #     3
    # 0     4
    #   2      8
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.view_tree()
    print('fnd=',tree.find(3).val)
    print('fnd=',tree.find(10))
    tree.delete_tree()
    tree.view_tree()

def create_BST_from_list(lst,view=False):
    tree = Tree()
    for lst1 in lst:
        tree.add(lst1)
    if view: print(tree)
    return tree

def tst_create_BST_from_list():
    lst=[5,8,9,2,1,3,7,4,6]
    print('ini sorted list = ',list(sorted(lst)))
    tr=create_BST_from_list(lst)
    tr.view_tree()

if __name__=="__main__":
    the_in_test()
    # tst_create_BST_from_list()