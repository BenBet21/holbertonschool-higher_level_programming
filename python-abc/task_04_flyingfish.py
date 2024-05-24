#!/usr/bin/env python3
'''Construct a FlyingFish class that inherits from \
both a Fish class and a Bird class'''


class Fish:
    '''this is Fish class'''
    def __init__(self):
        '''constructor'''
        Fish.__init__(self)

    def swim(self):
        '''swim method'''
        print("The flying fish is swimming")

    def habitat(self):
        '''habitat method'''
        print("The fish lives in water")


class Bird:
    '''this is Bird class'''
    def __init__(self):
        '''constructor'''
        Bird.__init__(self)

    def fly(self):
        '''fly method'''
        print("The bird is flying")

    def habitat(self):
        '''habitat method'''
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    '''class FlyingFish inherits from Fish and Bird'''
    def __init__(self):
        '''constructor'''
        pass

    def swim(self):
        '''swim method'''
        print("The flying fish is swimming!")

    def fly(self):
        '''fly method'''
        print("The flying fish is soaring!")

    def habitat(self):
        '''habitat method'''
        print("The flying fish lives both in water and the sky!")
