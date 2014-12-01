# encoding: utf-8

from datetime import timedelta
from datetime import date, datetime

from openerp import models, fields, api, _
from openerp.tools import cache
from openerp.exceptions import Warning
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

class Product(models.Model):
    u'''产品'''             #可选的描述文本，docstring 格式
    _name = 'sales.product' #定义模型的内部名称，必选具备

    name = fields.Char(u'名称', required=True, index=True)  #名称字段定义
    unit_price = fields.Float(u'单价', required=True)       #单价字段定义


class Customer(models.Model):
    u'''客户信息'''
    _name = 'sales.customer'

    name = fields.Char(u'姓名', required=True)
    address = fields.Char('联系地址')



class Order(models.Model):
    u'''销售订单'''
    _name = 'sales.order'

    name = fields.Char(u'单号', required=True)
    customer = fields.Many2one('sales.customer', u'客户', required=True)
    order_time = fields.Datetime(u'下单时间', required=True, default=fields.Datetime.now())
    lines = fields.One2many('sales.order.line', 'sales_order', u'订单明细')
    price_total = fields.Float(u'总价', compute='_sum_price')
    note = fields.Text(u'备注')

    @api.one
    @api.depends('lines')
    def _sum_price(self):
        price_total = 0.0
        for d in self.lines: 
            price_total += d.subtotal
        self.price_total = price_total
    

class OrderLine(models.Model):
    u'''销售订单明细'''
    _name = 'sales.order.line'

    sales_order = fields.Many2one('sales.order', u'订单', index=True, required=True, ondelete='cascade')
    name = fields.Many2one('sales.product', u'产品', required=True)
    quantity = fields.Float(u'数量', required=True)
    unit_price = fields.Float(u'单价', required=True)
    subtotal = fields.Float(u'小计', compute='_sum_subtotal')

    @api.one
    @api.depends('unit_price', 'quantity')
    def _sum_subtotal(self):
        self.subtotal = self.unit_price * self.quantity

    @api.onchange('name')
    def _onchange_product(self):
        self.unit_price = self.name.unit_price
        self.subtotal = self.unit_price * self.quantity

    @api.onchange('quantity', 'unit_price')
    def _onchange_qty_or_unit_price(self):
        self.subtotal = self.unit_price * self.quantity



