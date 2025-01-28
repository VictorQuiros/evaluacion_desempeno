# evaluacion_desempeno/__manifest__.py
{
    'name': 'Evaluación de Desempeño',
    'version': '1.0',
    'summary': 'Módulo para gestionar la evaluación de desempeño de los empleados',
    'category': 'Productivity',
    'author': 'Víctor Quirós',
    'website': 'https://tuweb.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'icon': '/evaluacion_desempeno/static/description/icon53.jpg',
    'data': [
    'views/evaluacion_desempeno_views.xml',
    'security/ir.model.access.csv',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'description': """Módulo de Odoo para la evaluación de desempeño de los empleados."""
}