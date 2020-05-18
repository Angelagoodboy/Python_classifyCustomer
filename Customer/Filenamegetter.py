#字典方式确定输出的文件夹 如../云联/ 用于与*.zip完成拼接
import Utils
class Filenamegetter:
    rule_path='' #规则文件路径
    def __init__(self,rule_path):
        self.rule_path=rule_path
    def getCustomerName(self):

