# evaluacion_desempeno/models/gestion_evaluacion_desempeno.py

from odoo import models, fields, api


class EvaluacionDesempeno(models.Model):
    _name = 'gestion.desempeno'
    _description = 'Evaluación del Empleado'

    name = fields.Char(string='Título de la Evaluación', required=True)
    comentarios = fields.Text(string='Comentarios del Evaluador')
    score = fields.Date(string = 'Puntuación', required=True, defult=1, help="Puntuación del 1 al 10", domain = [('score', '>=', 1), ('score', '<=', 10)])
    empleadoAsignado = fields.Many2one('hr.employee', string='Empleado Asignado')
    fechaEvaluacion = fields.Date(string='Fecha de Evaluación')

    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('in_progress', 'En Proceso'),
        ('completed', 'Finalizado'),
    ], string='Estado', default='pending')


    icon = fields.Char(string='Icono del Módulo')

    @api.model
    def create(self, vals):

        if not self.env.user.has_group('hr.group_hr_manager'):
            return super(EvaluacionDesempeno, self).create(vals)


    def write(self, vals):

        if not self.env.user.has_group('hr.group_hr_manager'):
            return super(EvaluacionDesempeno, self).write(vals)

    def unlink(self):

        if self.env.user.has_group('hr.group_hr_manager'):
            return super(EvaluacionDesempeno, self).unlink()


    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'completed':
            self.priority = '0'  # Baja prioridad si está completada
