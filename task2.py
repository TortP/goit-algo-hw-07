# Клас для вузла дерева
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Клас для двійкового дерева пошуку
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Вставка нового значення в дерево
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Рекурсивний метод для вставки значення
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Метод для знаходження найменшого значення
    def find_min_value(self):
        if self.root is None:
            raise ValueError("Дерево порожнє")
        return self._find_min(self.root)

    # Рекурсивний метод для пошуку найменшого значення
    def _find_min(self, node):
        current = node
        # Переходимо по лівим піддеревам, поки не дійдемо до кінця
        while current.left is not None:
            current = current.left
        return current.value

# Тестування
if __name__ == "__main__":
    tree = BinarySearchTree()
    # Вставка значень у дерево
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    # Знаходження найменшого значення
    print("Найменше значення в дереві:", tree.find_min_value())
