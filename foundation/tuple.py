#coding=utf-8
a = ('123',456,'abc')
print a[0]
print a[0:3]

#元组不可变，不能二次赋值，不支持增删
# del(a[0])

for item in a:
    print item

#空元组
a = ()
print a

#由于()可表示表达式优先级，为了避免歧义，所以单元素元组需要加个逗号
a = (1,)
print a
print a[0]

#'可变'的tuple,元组的指向不变，但指向的内容是可变的
l = [3,4]
a = (1,2,l)
print a
l[0] = 5
print a

print len(a)
