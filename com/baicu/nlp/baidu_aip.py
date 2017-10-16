# coding:utf8
from aip import AipNlp

# 定义常量
APP_ID = '9783460'
API_KEY = 'QgoHvvMmnoT7ocrayzEZn1lL'
SECRET_KEY = 'HBn7HD9kPUSuGIhl1ORvnmUIPCpcq0NF'

# 初始化AipNlp对象
aipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)

result = aipNlp.lexer('百度是个搜索公司')
for i in result:
    print i
result = aipNlp.wordSimEmbedding('漂亮', '美丽')

print result