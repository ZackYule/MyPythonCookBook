# 数据处理相关工具函数

### 导入库


```python
import numpy as np
from collections import Counter   #引入Counter
```

### 重复数据查找，并输出数据重复次数


```python
def find_duplicate_data(data_list):
    data_np = np.array(data_list)
    data_flat_list= data_np.flatten()
    data_count_dict = dict(Counter(data_flat_list))
    for key in list(data_count_dict.keys()):
        if data_count_dict[key] <= 1:
            data_count_dict.pop(key)
    return data_count_dict       
```

### 去重以及遍历，找出重复元素坐标


```python
def traversal(data_list):
    data_np = np.array(data_list)
    data_np_uniques = np.unique(data_np)
    duplicated_data = []
    for content in np.nditer(data_np_uniques):
        duplicated_data_coordinate = np.argwhere(data_np == content)
        if len(duplicated_data_coordinate) <= 1:
            continue
        duplicated_data.append({str(content): duplicated_data_coordinate})
    return duplicated_data
```

### 测试


```python
if __name__ == "__main__":
    data = [["a","b","c"],["a","d","a"]]
    print(find_duplicate_data(data))
    print(traversal(data))
    
```

    {'a': 3}
    [{'a': array([[0, 0],
           [1, 0],
           [1, 2]])}]

