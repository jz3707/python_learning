#!/usr/bin/env python
# coding=utf-8

# finally exception


def FinallyTest():
    """

    :return:
    """
    print 'i am starting....'

    while True:

        try:
            print 'i am starting....'
            raise IndexError('r')

        except NameError, e:
            print 'NameError happened %s', e

        finally:
            print 'finally executed'
            break


def ReturnTest(a):
    try:
        if a <= 0:
            raise ValueError('value error')
        else:
            return a

    except ValueError as e:
        print e

    finally:
        print 'The End!'
        return -1


if __name__ == '__main__':
    FinallyTest()
    print 'Return Testing :'
    print ReturnTest(0)
    print ReturnTest(2)
