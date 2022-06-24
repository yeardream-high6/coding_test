class Trie:
    def __init__(self):
        # [10] = is_terminal = True or False
        self.root = [None] * 10 + [False]

    def is_valid(self, number_str):
        curr = self.root
        for c in number_str:
            i = int(c)
            next_node = curr[i]
            if next_node == None:
                return True
            if next_node[10]:
                return False
            curr = next_node
        return False

    def add(self, number_str):
        curr = self.root
        for c in number_str:
            i = int(c)
            next_node = curr[i]
            if next_node == None:
                next_node = [None] * 10 + [False]
                curr[i] = next_node
            curr = next_node
        curr[10] = True

def solution(phone_book):
    trie = Trie()
    for phone_number in phone_book:
        if trie.is_valid(phone_number):
            trie.add(phone_number)
        else:
            return False
    return True
