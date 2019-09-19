import re

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
print(re.match('aaa','aaaabbb').group()) #在起始位置匹配
print(re.match('aaa','aaaabbb')) #不在起始位置匹配，返回None

# re.search 扫描整个字符串并返回第一个成功的匹配
print(re.search("haha","geinizhanggognzi").group())

# re.findall 从左到右扫描字符串，按顺序返回匹配，如果匹配你到则返回空列表
print(re.findall("\d","queshihenlihai"))
print(re.findall("\d","zhengchangfasheng"))

# sub用于替换
