# -*- coding: utf-8 -*-
'''
Created on 2014年11月25日

@author: heyuxing
'''
import xadmin
from xadmin.plugins.batch import BatchChangeAction

from book.models import Publisher,Book,Author

class PublisherAdmin(object):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')
    #点击可以进入编辑页面的字段
    list_display_links = ('name', 'address')
    #增加Publisher的向导
    wizard_form_list = [
        ('出版商名称', ('name',)),
        ('联系地址', ('address', 'city', 'state_province', 'country')),
        ('网站网址', ('website',))
    ]
    #该属性指定可以过滤的列的名字, 系统会自动生成搜索器
    list_filter = ['name'] 
    #设置搜索框和其模糊搜索的范围
    search_fields = ['name', 'address']
    #数据版本控制，默认记录10个版本，可以调整。恢复删除的数据
    reversion_enable = True
    
    #记录数据列表页面特定的数据过滤, 排序等结果. 添加的书签还可以在首页仪表盘中作为小组件添加
    #设置默认的书签. 用户可以在列表页面添加自己的书签, 你也可以实现设定好一些书签
    list_bookmarks = [{
        'title': "北京的出版社",         # 书签的名称, 显示在书签菜单中
        'query': {'gender': True}, # 过滤参数, 是标准的 queryset 过滤
        'order': ('-name'),         # 排序参数
        'cols': ('name', 'address', 'city'),  # 显示的列
        'search': '北京',   # 搜索参数, 指定搜索的内容
        'search_fields':'name',
        }, 
    ]
    
    #默认情况下, xadmin 会提供 Excel, CSV, XML, json 四种格式的数据导出.分别用 xls, csv, xml, json 表示 
    #TODO django1.7的bug mimetype改为content_type了，xadmin0.5还是用的mimetype
    list_export = ('xls', 'xml', 'json')
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
    #设置哪些字段要显示详细信息,
    show_detail_fields = ['name', 'address', ]
    #show_all_rel_details=True #设置时候自动显示所有关联字段的详细信息, 该属性默认为 True
    
    list_editable = ['address', 'city', ]
 
    #增加对列表中选中行的操作
    actions = [BatchChangeAction, ]
    #批量操作的对象的字段，BatchChangeAction中有该属性batch_fields的声明
    batch_fields = ('name', 'address')
    #指定 Field 的 Style， Style一般用来实现同一种类型的字段的不同效果，例如同样是 radio button，有普通及``inline``两种 Style。 
    #style_fields = {}
    #当 Model 是其他 Model 的 ref model 时，其他 Model 在显示本 Model 的字段时使用的 Field Style
    #relfield_style = 'fk-ajax'
 
class AuthorAdmin(object):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    reversion_enable = True
    
class BookAdmin(object):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #设置搜索栏范围，如果有外键，要注明外键的哪个字段，双下划线
    search_fields = ['title', 'publisher__address']
    reversion_enable = True
    #fields = ('title', 'authors', 'publisher', 'publication_date')
    #filter_horizontal = ('authors',)    #我们强烈建议针对那些拥有十个以上选项的`` 多对多字段`` 使用filter_horizontal。
    #raw_id_fields = ('publisher',)
       
xadmin.site.register(Publisher, PublisherAdmin)
xadmin.site.register(Author, AuthorAdmin)
xadmin.site.register(Book, BookAdmin)


