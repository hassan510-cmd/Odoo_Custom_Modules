from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'hospital.medicine'
    _description = 'Description'

    name = fields.Char()
    description = fields.Text(
        string="Description",
        required=False)

    usage_type = fields.Selection(
        string='Usage_type',
        selection=[('Tablet', 'Tablet'),
                   ('patches', 'patches'),
                   ('Liquid', 'Liquid'),
                   ('Capsules', 'Capsules'),
                   ('Injections', 'Injections'),
                   ],
        required=False, )

    barcode = fields.Char(
        string='Barcode',
        required=False)

    sale_price = fields.Float(
        string='Sale_price',
        required=False)

    scientific_name = fields.Char(
        string='Scientific_name',
        required=False)

    originator = fields.Char(
        string='Originator',
        required=False,

        )

    taxes = fields.Float(
        string='Taxes %',
        required=False,

        )

    sale_price_after_taxes= fields.Float(
        string='sale_price_after_taxes',
        required=False,
        compute='price_after_taxes'
        )

    def price_after_taxes(self):
        # print(self)
        # print(self.sale_price)
        # print(self.taxes)
        for record in self:
            record.sale_price_after_taxes=record.sale_price+(record.sale_price*record.taxes)
            # record.sale_price_after_taxes=30
            # print(record)


