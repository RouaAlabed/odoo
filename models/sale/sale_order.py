# -*- coding: utf-8 -*-
# Part of hunghn. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def export_quotation_xls(self):
        module = __name__.split('addons.')[1].split('.')[0]
        report_name = '{}.report_sale_order_xlsx'.format(module)
        report = {
            'type': 'ir.actions.report',
            'report_type': 'xlsx',
            'report_name': report_name,
            # model name will be used if no report_file passed via context
            'context': dict(self.env.context, report_file='sale_order'),
            # report_xlsx doesn't pass the context if the data dict is empty
            # cf. report_xlsx\static\src\js\report\qwebactionmanager.js
            # TODO: create PR on report_xlsx to fix this
            'data': {'dynamic_report': True},
        }
        return report
