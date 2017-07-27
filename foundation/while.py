#coding=utf-8
a = range(10)
i=0
while a[i]<5:
    print a[i]
    i = i + 1
print 'end'

while a[i]<8:
    print a[i]
    i = i + 1
    if a[i] > 5:
        break
print 'end'