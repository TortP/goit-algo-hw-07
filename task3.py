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

    # Метод для знаходження суми всіх значень у дереві
    def find_sum(self):
        return self._find_sum_recursive(self.root)

    # Рекурсивний метод для обчислення суми всіх значень у дереві
    def _find_sum_recursive(self, node):
        if node is None:
            return 0
        # Рекурсивно додаємо значення лівого і правого піддерев
        return node.value + self._find_sum_recursive(node.left) + self._find_sum_recursive(node.right)

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

    # Знаходження суми всіх значень у дереві
    print("Сума всіх значень у дереві:", tree.find_sum())
