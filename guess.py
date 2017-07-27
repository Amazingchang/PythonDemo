#coding=utf-8

def printNum():
    sInput = raw_input("请输入数字: ")
    try:
        nInput = int(sInput)
    except (ValueError,TypeError),diag:
        print str(diag)
    if nInput>100 or nInput<1:
        print "你数字不在范围之内，请重新输入"
    return nInput

def main():
    nInput = printNum()
    total = 1
    while nInput!=80:
        total += 1
        if nInput>80:
            print "大了"
        else:
            print "小了"
        nInput = printNum()
    print "猜对了"
    print "共猜了%d次" %total
main()


