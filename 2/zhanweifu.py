#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File		:	zhanweifu.py
@Time		:	2019/09/18 16:01:53
@Author		:	Icecarry
@Version	:	v1.0
@Contact	:	example@qq.com
@License	:	(C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc		:	None
'''

# here put the import lib


def main():
    # Write the executor here
    # %d 整数占位符,%d正常输出，%2d右对齐两位输出不够两位空格补齐
    # %02d和%2d差不多，右对齐两位输出，不够用0来补
    # %.2d输出整形时最少输出两位，不够用0来补
    print('%d,\n%2d,\n%02d,\n%.2d' % (1, 2, 3, 4))

    # %f 浮点数占位符默认占位小数点后六位
    # %20f 右对齐占位20，不够空格补齐
    # %020f 右对齐占位20，不够0补齐
    # %.2f 小数点后占位2位
    print('%0f,\n%20f,\n%020f,\n%.2f' % (1, 2, 3, 4))

    # %s 字符串占位符
    # name = input('请输入名字:')
    # print('名字是：%s' % name)

    # %x 十六进制整数占位符

    mark1 = 72
    mark2 = 85
    promote = (mark2-mark1)/mark1 * 100
    # 判断数据类型type()。
    print(type(promote))
    print('%.1f' % promote)
    # %转义字符为 %% ,format格式化输出应该可以自动转义
    print('hello %s,成绩提升了 %.1f %%' % ('小明', promote))
    print('hello {0},成绩提升了 {1:.1f} %'.format('小明', promote))

    # python3 除法为 / 和 // ,其中真除法为 / ,不管结果是否是整数,输出都为浮点数。
    # // 为地板除,两个都为整数，输出的结果为整数,结果取整为整型。如果任何一个数为浮点数，执行浮点数除法。
    # pyhton2 除法也有 / 和 // , 其中传统除法为 / ,
    # 如果两个都为整数，除数结果为整数，有小数取整后输出,如果任何一个数为浮点数,结果都为浮点数.
    # // 为地板除，和python3 一样，如果都为整数输出整数，有一个浮点数，执行浮点数除法。
    a = 4
    b = 2
    d = 3
    f = 3.0
    c = a / b
    e = d // a
    g = f // a
    print(c)
    print(type(c))
    print(e)
    print(type(e))
    print(g)
    print(type(g))


if __name__ == '__main__':
    main()
