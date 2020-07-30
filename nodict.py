#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Joseph Padgett'


class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.hash = hash(self.key)
        self.value = value
        # Your code here
        

    def __repr__(self):
        # Your code here
        return f"{self.__class__.__name__}({self.key}, {self.value})"

    def __eq__(self, other):
        if self.key == other.key:
            return True
        else:
            return False

class NoDict:
    def __init__(self, num_buckets=10):
        self.buckets =  [[] for i in range(num_buckets)]
        # Your code here
        self.size = num_buckets

    def __repr__(self):
        # Your code here
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        # Your code here
        im_up_in_your_wagon = Node(key, value)
        bucket = self.buckets[im_up_in_your_wagon.hash % self.size]
        for each in bucket:
            if each == im_up_in_your_wagon:
                bucket.remove(each)
                break
        bucket.append(im_up_in_your_wagon)

    def get(self, key):
        # Your code here
        i_hold_the_keys = Node(key)
        bucket = self.buckets[i_hold_the_keys.hash % self.size]
        for thang in bucket:
            if thang == i_hold_the_keys:
                return thang.value
        raise KeyError(f'{key} was not found')

    def __getitem__(self, key):
        # Your code here
        return self.get(key)

    def __setitem__(self, key, value):
        # Your code here
        return self.add(key, value)

n1 = Node('Mike', 21)
n2 = Node('Mike', 34)
n3 = Node('Nick', 56)
print(f'n1 == n2 ? {n1 == n2}')
print(f'n2 == n3 ? {n2 == n3}')