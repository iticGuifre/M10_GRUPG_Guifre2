# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employees(models.Model):
    _name = 'employees.employees'
    _description = 'employees.employees'

    name = fields.Char()
    last_name = fields.Char()
    description = fields.Text()
    date_of_birth = fields.Char()
    gender = fields.Char()
    nationality = fields.Char()
    email = fields.Char()
    phone = fields.Integer()
    address = fields.Char()
    employee_id = fields.Integer()
    department_id = fields.Integer()
    job_title = fields.Char()
    date_hired = fields.Char()
    

