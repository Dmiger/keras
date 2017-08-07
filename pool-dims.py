# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 17:06:02 2017

@author: Sony VAIO Pro
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head