from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Evaluación de Desempeño'

    name = fields.Char(string='Título de la Evaluación', required=True)
    comentarios = fields.Text(string='Comentarios del Evaluador')
    score = fields.Float(string='Puntuación', required=True, default=1.0, help="Puntuación del 1 al 10")
    empleadoAsignado = fields.Many2one('hr.employee', string='Empleado Asignado')
    fechaEvaluacion = fields.Date(string='Fecha de Evaluación')

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_progress', 'En Proceso'),
        ('done', 'Hecho'),
    ], string='Estado', default='draft')

    priority = fields.Integer(string='Prioridad', default=1)
    icon = fields.Char(string='Icono del Módulo')

    def iniciar_evaluacion(self):
        self.state = 'in_progress'

    def finalizar_evaluacion(self):
        self.state = 'done'

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'completed':
            self.priority = 0  # Baja prioridad si está completada
