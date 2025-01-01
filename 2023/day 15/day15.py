from collections import defaultdict


class item:
    def __init__(self, label, lens):
        self.label = label
        self.lens = lens
        self.next = None
        self.prev = None


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item: item):
        node = self.head

        while node:
            if node.label == item.label:
                node.lens = item.lens
                return
            node = node.next

        if self.head and self.tail:
            self.tail.next = item
            item.prev = self.tail
            self.tail = item
        else:
            self.head = item
            self.tail = item

    def remove(self, label):
        node = self.head

        while node:
            if node.label == label:
                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                if node == self.head:
                    self.head = node.next
                if node == self.tail:
                    self.tail = node.prev
                return
            node = node.next

    def empty(self):
        return not self.head


def get_hash(sequence):
    c = 0

    for s in sequence:
        c += ord(s)
        c *= 17
        c %= 256

    return c


def part_two(sequences):
    hash_table = defaultdict(linked_list)
    count = 0

    for sequence in sequences:
        if sequence[-2] == "=":
            hash_table[get_hash(sequence[:-2])].add(
                item(sequence[:-2], int(sequence[-1]))
            )

        else:
            hash_table[get_hash(sequence[:-1])].remove(sequence[:-1])

    for i in range(256):
        if i in hash_table and not hash_table[i].empty():
            slot = 1
            node = hash_table[i].head

            while node:
                count += (i + 1) * slot * node.lens
                slot += 1
                node = node.next

    return count


sequences = open("input.txt").read().split(",")
print(f"Part one: {sum(map(get_hash, sequences))}")
print(f"Part two: {part_two(sequences)}")
