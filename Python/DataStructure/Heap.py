class Heap(object):
    def __init__(self):
        self.data_list = list()

    def size(self):
        return len(self.data_list) - 1

    def left_child(self, root):
        return root * 2

    def right_child(self, root):
        return root * 2 + 1

    def father(self, node):
        return node / 2

    def heapify(self, root):
        if root > self.size():
            return
        left_node = self.left_child(root)
        right_node = self.right_child(root)
        largest = root
        if left_node <= self.size():
            if self.data_list[left_node] > self.data_list[largest]:
                largest = left_node
        if right_node <= self.size():
            if self.data_list[right_node] > self.data_list[largest]:
                largest = right_node
        if largest != root:
            self.data_list[root], self.data_list[largest] = self.data_list[
                largest], self.data_list[root]
            self.heapify(largest)

    def build_heap(self):
        for i in range(int(self.size() / 2), 0, -1):
            self.heapify(i)

    def get_max(self):
        if self.size() == 0:
            return '堆栈为空'
        ret = self.data_list[1]
        self.data_list[1] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify(1)
        return ret

    def insert(self, data):
        self.data_list.append(data)
        now_index = int(self.size())
        pre = int(self.father(now_index))
        while self.data_list[pre] < data and now_index != 1:
            self.data_list[pre], self.data_list[now_index] = self.data_list[
                now_index], self.data_list[pre]
            now_index = pre
            pre = int(now_index / 2)


heap = Heap()
heap.insert(9)
heap.insert(10)
heap.insert(7)
heap.insert(12)
heap.insert(3)
heap.insert(4)
heap.insert(8)
print(heap.data_list)
print(heap.get_max())
print(heap.get_max())
print(heap.get_max())
print(heap.get_max())
print(heap.get_max())
print(heap.get_max())
print(heap.get_max())
print(heap.data_list)

heap.data_list = [None, 1, 2, 3, 4, 5, 6, 7]
heap.build_heap()
print(heap.data_list)
print(heap.get_max())
