# 一个用于批量处理文件的代码仓库

>请使用较新的python版本以避免注解出错

### 目前功能:

#### 1.批量移动文件
将一个目录下的所有文件移除子目录并转移到新的文件中
```python
import move_file as mvf

src = r""
dst = r""
mvf.copy_all(src, dst, by_suffix=False)
# ########################################
mission = mvf.CopyMission(src, dst)
mission.run()
```
根据文件后缀将文件分别存放
```python
import move_file as mvf

src = r""
dst = r""
mvf.copy_all(src, dst, by_suffix=True)
# ########################################
mission = mvf.CopyMission(src, dst)
mission.sort_by_suffix()
mission.run()
```
仅存放文件名中包含指定字符串的文件
```python
import move_file as mvf

src = r""
dst = r""
mission = mvf.CopyMission(src, dst)
mission2 = mvf.CopyMission(src, dst)
kw = "test"

kw2 = ["word1", "word2"]

mission.filter_by_name(kw)
mission2.filter_by_name(kw2)

mission.run()
mission2.run()
```