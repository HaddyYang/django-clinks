# 自定义链接提取和写入
该项目是基于Django2.0开发的Django应用。Django1.x也可以用。

其主要用途是SEO，实现提取文章的自定义链接、写入自定义链接和编辑自定义链接等功能。


## 安装方法
1. 该项目是Django的app。需要把该app整个文件夹复制到你的Django项目中
2. settings的INSTALLED_APPS 添加该应用
```
INSTALLED_APPS = [
    '...',  # 其他应用
    'clinks',
]
```
3. 执行```python manage.py migrate```
4. 可登录admin，可以看到clink应用


## 使用示例(二选一)
### 示例1、调用save()方法之前
```
from clinks.utils import extract_custom_links, write_into_custom_links

extract_custom_links(blog.content)
blog.content = write_into_custom_links(blog.content)
blog.save()
```

### 示例2、使用Signals方法
该方法可以让我们在admin管理界面使用。需要在具体的应用中使用signals。

若不懂怎么使用，可以参考我的[Django2.0教程第44节](https://www.bilibili.com/video/av42276162)。

假设该对象的content字段需要处理，如下示例代码:
```
from django.db.models.signals import pre_save
from django.dispatch import receiver
from clinks.utils import extract_custom_links, write_into_custom_links  # 导入自定义链接处理的两个方法
from blog.models import Blog  # 具体要处理的模型对象

@receiver(pre_save, sender=Blog)
def custom_links_signal(sender, intance, **kwargs):
    if intance.created == True:  # 判断是否是新建
        extract_custom_links(intance.content)
        intance.content = write_into_custom_links(intance.content)
```

如果觉得上面两个方法名称过长，也可以引用clinks.utils中的ClinksUtils类
```
from clinks.utils import ClinksUtils

cu = ClinksUtils()
cu.extract(blog.content)  # 提取自定义链接
content = cu.write_into(content)  # 写入自定义链接
```


## 更新说明
- v0.1版
    - 建立自定义链接模型
    - 添加提取自定义链接和写入自定义链接功能
    - 不足：写入自定链接功能使用replace方法直接替换。该方法不能处理一些特殊情况，下个版本更新。