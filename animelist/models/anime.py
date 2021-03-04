#-*- coding: utf-8 -*-
from odoo import models, fields, api

class Anime(models.Model):
    _name = 'animelist.anime'
    titulo = fields.Char('Titulo', required=True)
    nota = fields.Float('Nota', required=True)
    genero_principal = fields.Char('Genero Principal', required=True)
    creador = fields.Char('Creador', required=True)
    temporadas = fields.Integer('Temporadas', required=True)