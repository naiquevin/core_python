#!/usr/bin/env python

from sys import argv

class AddrBookEntry(object):
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph

    def updatePhone(self, ph):
        self.phone = ph

class EmplAddrBookEntry(AddrBookEntry):
    def __init__(self, nm, ph, empid, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = empid
        self.email = em

    def updateEmail(self, em):
        self.email = em

def bound_unbound():
    # Calling bound and unbound methods
    a = EmplAddrBookEntry('vineet', '9820776899', 2334, 'vineet@gmail.com')
    a.updateEmail('naikvin@gmail.com')
    print a.email
    # unbound method call requires the instance to be passed explicitly
    EmplAddrBookEntry.updateEmail(a, 'naikvin@example.com')
    print a.email
    # an instance is always required while method invocation

def attrs():
    print '__name__ %s' % EmplAddrBookEntry.__name__
    print '__doc__ %s' % EmplAddrBookEntry.__doc__
    print '__bases__ %s' % EmplAddrBookEntry.__bases__
    print '__module__ %s' % EmplAddrBookEntry.__module__
    print '__dict__ %s' % EmplAddrBookEntry.__dict__

def delete():
    """
    Example showing how python's garbage collection affects the behaviour of __del__ method
    """

    class P(object):
        # def __del__(self):
        #     pass
        # TODO find why this fails with Exception
        pass

    class C(P):
        def __init__(self):
            P.__init__(self)
            print 'initialized'

        def __del__(self):
            P.__del__(self)
            print 'object dellocated'

    c1 = C()
    c2 = c1
    c3 = c2    
    print id(c1)
    print id(c2)
    print id(c3)
    del c1
    print 'c1 ref removed'
    del c2
    print 'c2 ref removed'
    del c3
    print 'c3 ref removed'

def class_attr():
    """
    Behaviour of and interaction with the class attributes in python oop
    """
    class C(object):
        foo = 1.2
        
    c = C()
    print "Original value of C.foo is set to %0.2f" % C.foo
    print "C.foo > %f" % C.foo
    print "C.foo accessed through the intance as c.foo"
    print "c.foo > %0.2f" % c.foo
    print "However, updates to the class attribute is only allowed through the class"
    print ">> C.foo += 1"
    C.foo += 1
    print c.foo
    print "If a we try to update Class attr using the instance, it results in the creation of an instance attribute"
    print ">> c.foo += 10"
    c.foo += 10
    print "So now, c.foo has the value of the instance variable"
    print "c.foo > %0.2f" % c.foo
    print "Whereas C.foo will continue to hold the old value"
    print "C.foo > %0.2f" % C.foo
    print "If c.foo is deleted at this moment, it will again start showing the old value"
    del c.foo
    print "c.foo > %0.2f" % c.foo
    print "Such behaviour is observed because in python, a Class and an Instance both have their own __dict__"
    print "But while reading an attribute, python first tries to find in class, then in instance, then base classes"
    print "In python 'explicit is better than implicit'"
    print "So always modify class attr using class name and instance attr using instance name!"

if __name__ == '__main__':
    script, func_name = argv
    # convert function name (str) to callable function object
    mod = __import__('oop')
    func = getattr(mod, func_name)
    func()
