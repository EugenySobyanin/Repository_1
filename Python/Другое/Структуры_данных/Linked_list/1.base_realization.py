# создаем класс ноды
class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
        

class LinkedList:
    def __init__(self, root) -> None:
        self.root = root
    
    def append(self, new_val):
        # Добавление элемента в конец списка.
        tmp = self.root
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val=new_val)
        
    def output(self):
        # Вывод связного списка
        tmp = self.root
        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.next
        print()
        
    def search(self, val) -> bool:
        # Поиск элемента
        tmp = self.root
        while tmp:
            if tmp.val == val:
                return True
            tmp = tmp.next
        return False
    
    def pop(self):
        tmp = self.root
        if tmp.next.next:
            while tmp.next.next:
                tmp = tmp.next
            tmp.next = None
            
    def reverse(self):
        prev = None
        current = self.root
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.root = prev      
        
root = Node(10)
linked_list = LinkedList(root=root)
linked_list.append(15)
linked_list.append(30)
linked_list.output()
linked_list.pop()
linked_list.output()
linked_list.append(16)
linked_list.append(17)
linked_list.append(18)
linked_list.output()
linked_list.reverse()
linked_list.output()
