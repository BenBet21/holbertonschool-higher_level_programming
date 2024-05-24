#!/usr/bin/env python3
'''Design two mixin classes, SwimMixin and FlyMixin, \
each equipped with methods swim and fly respectively'''


class SwimMixin:
    '''this is SwimMixin class'''
    def swim(self):
        '''swim method'''
        print("The creature swims!")


class FlyMixin:
    '''this is FlyMixin class'''
    def fly(self):
        '''fly method'''
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    '''this is Dragon class that inherits from SwimMixin and FlyMixin'''
    def roar(self):
        '''roar method'''
        print("The dragon roars!")
