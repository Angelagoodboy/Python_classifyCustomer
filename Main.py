#调用Python文件并且实现输入不同参数对应不同分类组合
import  sys
#实现脚本上输入参数
def main():
    try:
        Type=sys.argv[1]
        FileInputpath=sys.argv[2]
        FileOutpupath=sys.argv[3]
        if Type=='-r':
            # 调用客户模块：


    except  IndexError as e:
        print("输入的错误参数")







if __name__ == '__main__':
    print('helloworld')
    main()



