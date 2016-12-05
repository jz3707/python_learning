#!/usr/bin/env python
# coding=utf-8

# finally exception


def FinallyTest():
    """

    try中raise IndexError之后except没能捕获这个exception
    系统会将这个exception临时保存起来
    当finally执行结束的时候，临时保存起来的exception会再次被跑出
    但是如果finally中有return，break，那么临时保存的exception就会丢失
    从而导致异常屏蔽

    所以这个function的结果是：
        i am starting....
        i sm starting....
        finally executed

    :return:
    """
    print 'i am starting....'

    while True:

        try:
            print 'i am starting....'
            raise IndexError('r')

        except NameError as e:
            print 'NameError happened %s', e

        finally:
            print 'finally executed'
            break


def ReturnTest(a):

    """

    a = 0,
    try跑出异常，except中捕获了这个ValueError，并处理
    然后执行finally section。

    a = 2
    try 进入else模块，在return a之前进入finnaly section，
    并return -1

    所以结果：
        -1
        -1

    :param a:
    :return:
    """
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


