#-*- coding: utf-8 -*-
from odoo import models, fields, api

class Prota(models.Model):
    _name = 'animelist.prota'
    nombre = fields.Char('Nombre', required=True)
    sexo = fields.Char('Sexo', required=True)
    edad = fields.Integer('Edad', required=True)
    arma = fields.Char('Arma', required=True)