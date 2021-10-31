# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",

    'summary': "Hospital Management System",
    'sequence' : 1,

    'description': "Hospital Management System",

    'author': "My Company",
    'website': "https://codeclinic.ml",
    'application' :True,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/patient.xml',
        'views/saleorder.xml',
        'views/parent.xml',
        'views/medicine.xml',
        'data/patient_seq.xml',
        'views/medicine_order.xml',
        'views/sale_medicine_invoice.xml',
        'views/kids.xml',
        'views/patient_gender.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
