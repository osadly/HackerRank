#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def reverse(llist):
    if llist==None:
        return llist
    
    '''
    #hlprList=[llist.data]
    prvs=llist
    crntOrgn=llist.next
    while crntOrgn != None:
        #print(prvs.data)
        tmp = crntOrgn.next
        crntOrgn.next = prvs
        prvs = crntOrgn
        crntOrgn = tmp
        
    #print(prvs.data)
    return prvs    
    #for i in range(len(hlprList)-1,-1):
    '''
    myList=[]
    while 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
