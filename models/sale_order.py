from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    number = fields.Integer(string='Sequence', compute='_compute_number_line')

    def _compute_number_line(self):
        i = 1
        for record in self:
            record.number = i
            i = i + 1




