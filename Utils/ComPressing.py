#实现压缩功能
import  zipfile
class ComPresser:

    def Press(self,zip_name,file):
        zp=zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
        zp.write(file)
        zp.close()
        print('压缩成功')

if __name__ == '__main__':
    CP=ComPresser()
    CP.Press('text.zip','text.txt')