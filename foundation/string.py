#coding=utf-8
a = "aaaaa"
print a

#转义字符
a = "\'"
print a

#raw字符串
a = r'\(~_~)/ \(~_~)/'
print a

#字符串方法
print len(a)
print a[1]
print a[1:5]
print '(' in a
print a * 2

print a[:-1]
for item in a:
    print item