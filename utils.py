# utils： 工具集
# 1、提取新的自定义链接保存到数据库
# 2、写入自定义链接到文章

import re
from django.utils.html import strip_tags
from .models import CustomLink


# 提取自定义链接
def extract_custom_links(content):
    add_count = 0
    regexp = r'<a.+?href=[\'"](.+?)[\'"].*?>(.+?)</a>'
    # 匹配内容的a标签
    for href, text in re.findall(regexp, content):
        # 去掉text的html标签，保留文字
        text = strip_tags(text)
        if text != '':
            # 判断a标签是否在数据库中
            if not CustomLink.objects.exsits(text=text):
                # 插入数据库
                CustomLink.add(link=href, text=text)
                add_count += 1
    return add_count

# 写入自定义标签到内容
def write_into_custom_links(content):
    # 特殊情况：a标签不能包含a标签。很多意外情况，都是这个问题导致的
    # 1、考虑用正则。 匹配文字，该文字不在a标签中
    # 2、考虑用xpath
    for clink in CustomLink.objects.all():
        a_tag = '<a href="{link}">{text}</a>'.format(link=clink.link, text=clink.text)
        content = content.replace(clink.text, a_tag)
    return content


# 如果觉得上面两个函数名字过长，也可以使用这个封装的类
# cu = ClinksUtils()
# cu.extract(blog.content)
# content = cu.write_into(content)
class ClinksUtils():
    def extract(self, content):
        return extract_custom_links(content)

    def write_into(self, content):
        return write_into_custom_links(content)
