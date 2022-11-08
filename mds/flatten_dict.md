# 字典扁平化函数(外加性能测试)

### 定义测试数据


```python
data = {'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8], 'e':[{'f':9},{'h':10}]}
```

### 加载库


```python
%load_ext memory_profiler
```

### 第三种方法
##### 代码


```python
def flatten_map(src):
    def _flatten_map(src,dest=None,prefix=''):
        if isinstance(src,dict):
            for k,v in src.items():
                if isinstance(v,(list,tuple,set,dict)):
                    _flatten_map(v,dest,prefix=prefix+k+'.') #递归调用
                else:
                    dest[prefix+k] = v
        else:
            for i, v in enumerate(src):
                if isinstance(v,(list,tuple,set,dict)):
                    _flatten_map(v,dest,prefix=prefix+str(i)+'.') #递归调用
                else:
                    dest[prefix+str(i)] = v
    dest = {}
    _flatten_map(src,dest)
    return dest
```

##### 测试代码


```python
flatten_map(data)
```


```python
%%timeit
flatten_map(data)
```


```python
%memit
flatten_map(data)
```

### 简易库方法

##### 代码


```python
import flatdict

flatdict.FlatDict(data, delimiter='.')
```

##### 性能测试


```python
%%timeit
flatdict.FlatDict(data)
```


```python
%memit
flatdict.FlatDict(data)
```

### 自定义方法

##### 代码


```python
from collections.abc import MutableMapping

def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str ='.') -> MutableMapping:
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
```

##### 测试效果：


```python
flatten_dict(data)
```


```python
%%timeit
flatten_dict(data)
```


```python
%memit
flatten_dict(data)
```
