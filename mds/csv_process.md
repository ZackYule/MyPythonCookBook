# csv&xlsx 处理代码

### 初始设定


```python
import sys
import os
import openpyxl
import csv
import re
from loguru import logger
logger.remove()
handler_id = logger.add(sys.stderr, level="DEBUG")
```

### csv读取

##### 按列读取


```python
def get_column_info_from_csv(file_path:str, column_num:int)->list[dict]:
    if not os.path.isfile(file_path):
        logger.debug(file_path)
        logger.info('没有找到读取文件')
        return []
        
    items = []
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        is_first_read = True
        for row in reader:
            if is_first_read:
                is_first_read = False
                continue
            items.append(row[column_num])
    return items
```

##### 全部读取


```python
def get_content_info_from_csv(file_path:str)->list[dict]:
    if not os.path.isfile(file_path):
        logger.info('没有找到读取文件')
        return []
    
    items = []
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)
    return items
```

##### 测试


```python
title = "测试一下" 
content_type = "的知乎回答表"
base_dir = '..' + os.sep + 'resource'
file_path = base_dir + os.sep + title + content_type + '.csv'
id_list = get_column_info_info_from_csv(file_path, 7)
item_list = get_content_info_from_csv(file_path)
print(id_list)
print(len(item_list))
```

    ['2175447907']
    1


### csv 写入


```python
def csv_pipeline(item:dict, keyword:str, content_type:str, header:list[str]):
    base_dir = '结果文件' + os.sep + keyword
    file_path = base_dir + os.sep + keyword + content_type + '.csv'

    if not os.path.isdir(base_dir):
        os.makedirs(base_dir)
    if not os.path.isfile(file_path):
        is_first_write = 1
    else:
        is_first_write = 0
        
    if item:
        with open(file_path, 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            if is_first_write:
                if header:
                    writer.writerow(header)
            writer.writerow([item[key] for key in item.keys()])
```

### csv wash


```python
def del_tag(string):
    tag_del_patten = re.compile(r'<.*?>')
    res = tag_del_patten.sub('', string)
    res = res.replace('\u3000', '')
    return res


def single_line_process(string_list, string_process_func):
    res = []
    for string in string_list:
        new_string = string_process_func(string)
        res.append(new_string)
    return res


def write_new_csv(old_file_path, new_row_list):
    file_path = old_file_path + '_new.csv'
    with open(file_path, 'a', encoding='utf-8-sig', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(new_row_list)


def csv_transformer(file_path:str, string_process_func):
    with open(file_path, encoding='utf-8-sig', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            new_row = single_line_process(row, string_process_func)
            write_new_csv(title, new_row)
```

##### 实验运行


```python
file_path = '../resource' + os.sep + '十九届六中全会的知乎专栏文章表' + '.csv'
csv_transformer(file_path, del_tag)
```

### xlsx 表格 读取


```python
def get_content_from_xlsx(file_path:str, sheet_name:str,column_num:int):
    # excel表格对象 与 sheet对象
    xlsx_el = openpyxl.load_workbook(file_path)
    sheet_el = xlsx_el[sheet_name]
    # 读取
    result = []
    row_num = sheet_el.max_row
    for i in range(row_num):
        target_value = sheet_el.cell(row=i+1, column=column_num).value
        if target_value:
            result.append(target_value)
    
    xlsx_el.close()
    return result
```

##### 测试


```python
file_path = '..' + os.sep + 'resource' + os.sep + 'weibo.xlsx'
sheet_name = 'weibo'
res = get_content_from_xlsx(file_path, sheet_name, 1)
print(res[1:10])
```

    ['领事闲谈', '汇跑赛事', '张蛋蛋的酒窝没有酒', '-冰淇淋流泪', '最优生记录本', '跳大海乐队', 'Justin黄明昊的宣宣', '王俊凯官后陕西分会', '杯羹文史']

