class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.val:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._find_min(node.right)
            node.val = temp.val
            node.right = self._delete_recursive(node.right, temp.val)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")

    def __str__(self):
        return "Binary Tree"

# Пример использования бинарного дерева
if __name__ == "__main__":
    bt = BinaryTree()

    # Вставка элементов
    bt.insert(50)
    bt.insert(30)
    bt.insert(20)
    bt.insert(40)
    bt.insert(70)
    bt.insert(60)
    bt.insert(80)

    print("Прямой обход (Preorder):")
    bt.preorder(bt.root)  # 50 30 20 40 70 60 80
    print("\n")

    print("Симметричный обход (Inorder):")
    bt.inorder(bt.root)  # 20 30 40 50 60 70 80
    print("\n")

    print("Обратный обход (Postorder):")
    bt.postorder(bt.root)  # 20 40 30 60 80 70 50
    print("\n")

    # Поиск элемента
    search_key = 60
    result = bt.search(search_key)
    if result:
        print(f"Элемент {search_key} найден в дереве.")
    else:
        print(f"Элемент {search_key} не найден в дереве.")

    # Удаление элемента
    delete_key = 30
    print(f"Удаление элемента {delete_key}...")
    bt.delete(delete_key)

    print("Симметричный обход после удаления:")
    bt.inorder(bt.root)  # 20 40 50 60 70 80
    print("\n")