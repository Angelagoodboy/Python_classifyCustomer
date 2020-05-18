#1.读取文件内容 忽略#后内容
class ruleReader:
    def getCustomerName(self,rule_path):
        f=open(rule_path,'r',1)
        f.read()
