# -*- coding: utf-8 -*-

from odoo import models, fields, api


class m10test(models.Model):
    _name = 'm10test.m10test'
    _description = 'm10test.m10test'

    name = fields.Char()
    quantity = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    state = fields.Selection([
        ('preparing', 'Preparing'),
        ('shipped', 'Shipped'),
        ('received', 'Received'),
        ('returned', 'Returned'),
    ], string="State", default='preparing')

    product_code = fields.Char()
    product_category = fields.Char()
    lot_number = fields.Integer()
    expiration_date = fields.Date(string = "Expiration date")
    weight = fields.Integer()
    dimensions = fields.Char()
    color = fields.Char()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
