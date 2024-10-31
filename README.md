# 一个用于批量处理文件的代码仓库

>请使用较新的python版本以避免注解出错

### 目前功能:

#### 1.批量移动文件
  - 根据文件后缀划分

```python
import move_file as f

if __name__ == "__main__":
    src = "INSERT YOUR SOURCE DIRECTORY HERE"
    dst = "INSERT YOUR DESTINATION DIRECTORY HERE"
    f.copy_all(src, dst, by_suffix=True, verbose=True)

```