# 引入python基础库
import re
import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mlxtend.preprocessing import TransactionEncoder

import seaborn as sns

# 查看数据表格式和基本信息
from platformdirs.windows import Windows

input_data = pd.read_csv('D://Data Science/GLIS630/Final project/Fashion Survey Data/project/data/merge.csv', encoding='gbk')

print(input_data.info())
print(input_data.head(10))
print(input_data.describe())

df = pd.DataFrame(data=input_data)

# 对于Device type选择windows用户的20%替换为apple用户
#查找有windows的数量
print(df['DeviceType'].value_counts())

#list to dict
def convert(a):
    it = iter(a)
    res_dict = dict(zip(it, it))
    return res_dict

#指定查找列
value = input_data['DeviceType']

#从list转成dic
convert_value = convert(value)

print(convert_value)

#遍历每一个含‘windows’的值，随机选择其中的43个，替换成iPhone/iPad
for x in value:
    if x == 'Windows':
        randomValue = random.sample(list(convert_value), k=43)
        replaceValue = re.sub(r'Windows', "iPhone/iPod", randomValue)

        print(replaceValue)




#选择随机20%的数量， 用正则表达式替换
'''randomValue = value.random.sample(value, 43)

replaceValue = re.sub(r'Windows', "iPhone/iPod", randomValue)

print(data.head(10))
'''




"""def random(value):
    value = [["DeviceType"]]
    random_value = []

    for i in value:
        if value.str.contains("Windows"):
            i = random.sample(value, 43)"""

