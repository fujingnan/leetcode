# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。 
# 
#  
#  
#  实现 LRUCache 类： 
# 
#  
#  LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存 
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
#  void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上
# 限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 
#  
# 
#  
#  
#  
# 
#  进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？ 
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 3000 
#  0 <= value <= 104 
#  最多调用 3 * 104 次 get 和 put 
#  
#  Related Topics 设计 
#  👍 1098 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.lru = {}
#         self.used = []
#         self.cache = []
#
#     def get(self, key: int) -> int:
#         if not key in self.lru:
#             return -1
#         else:
#             self.used.append(key)
#             return self.lru[key]
#
#     def put(self, key: int, value: int) -> None:
#         if len(self.lru) < self.capacity:
#             self.lru[key] = value
#             self.cache.append(key)
#             self.used.append(key)
#         else:
#             i, d = 0, self.used[0]
#             while i < len(self.cache) and self.cache[i] in self.used:
#                 i += 1
#             if i == len(self.cache):
#                 del self.lru[self.used[0]]
#                 self.lru[key] = value
#                 self.used = [x for x in self.used[1:]]
#                 self.cache = [x for x in self.cache if not x == d]
#             else:
#                 del self.lru[self.cache[i]]
#                 self.lru[key] = value
#                 self.cache = [x for x in self.cache if not x == self.cache[i]]
#             self.cache.append(key)
#             self.used.append(key)

class DLinkedNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def add_node_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def move_node_to_head(self, node):
        self.remove_node(node)
        self.add_node_to_head(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.move_node_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if not key in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.add_node_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                r_node = self.remove_tail()
                self.cache.pop(r_node.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = value
            self.move_node_to_head(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
