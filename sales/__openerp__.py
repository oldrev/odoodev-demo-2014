#encoding: utf-8

{
    'name': u'销售订单管理开发实例', #模块名称，必填
    'version': '0.1', #版本
    'depends': ['base', 'web'], #依赖的模块
    'category' : 'Demo', #模块分类
    'summary': 'Odoo 简单模块开发例子：销售订单管理', #模块简介
    'description': """""", #模块描述
    'author': 'YourName', #作者
    'website': 'http://www.sandwych.com', #
    'data': [
        'sales_view.xml', #初始化模块或者升级模块时导入的数据
    ],
    'demo': [], #这里指定演示数据
    'installable': True, #模块是否可通过管理界面安装
    'images': [], #指定模块的图标等
}


