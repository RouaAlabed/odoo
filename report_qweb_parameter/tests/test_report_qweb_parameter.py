# -*- coding: utf-8 -*-
# Copyright 2017 Creu Blanca
<<<<<<< HEAD
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
=======
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
>>>>>>> [ADD] report_field_length

import xml.etree.ElementTree as ET

from odoo.addons.base.ir.ir_qweb import QWebException
from odoo.tests import common


class TestReportQWebParameter(common.TransactionCase):
    def test_qweb_parameter(self):
<<<<<<< HEAD
        report_name = 'report_qweb_parameter.test_report_length'
        report_obj = self.env['ir.actions.report']
        report_object = report_obj._get_report_from_name(report_name)

        docs = self.env['res.company'].search([], limit=1)
        vat = docs.vat
        website = docs.website
        street = docs.street
        company_registry = docs.company_registry
        docs.update({
            'street': '12345678901',
=======
        report_object = self.env['ir.actions.report.xml']
        report_name = 'report_qweb_parameter.test_report_length'
        docs = self.env['res.company'].search([], limit=1)
        vat = docs.vat
        website = docs.website
        fax = docs.fax
        company_registry = docs.company_registry
        docs.update({
            'fax': '12345678901',
>>>>>>> [ADD] report_field_length
            'vat': '12345678901',
            'website': '1234567890',
            'company_registry': '1234567890'
        })
<<<<<<< HEAD
        rep = report_object.render(docs.ids, False)
        root = ET.fromstring(rep[0])
        self.assertEqual(root[0].text, "1234567890")
        self.assertEqual(root[2].text, "1234567890")
        docs.update({'street': '123456789'})
        with self.assertRaises(QWebException):
            report_object.render(docs.ids, False)
        docs.update({'street': '1234567890', 'vat': '123456789'})
        with self.assertRaises(QWebException):
            report_object.render(docs.ids, False)
        docs.update({'vat': '1234567890', 'website': '12345678901'})
        with self.assertRaises(QWebException):
            report_object.render(docs.ids, False)
        docs.update(
            {'website': '1234567890', 'company_registry': '12345678901'})
        with self.assertRaises(QWebException):
            report_object.render(docs.ids, False)
        docs.update({
            'street': street,
=======
        rep = report_object.render_report(docs.ids, report_name, False)
        root = ET.fromstring(
            rep[0]
            )
        self.assertEqual(root[1][0][0][0].text, "1234567890")
        self.assertEqual(root[1][0][0][2].text, "1234567890")
        docs.update({'fax': '123456789'})
        with self.assertRaises(QWebException):
            report_object.render_report(docs.ids, report_name, False)
        docs.update({'fax': '1234567890', 'vat': '123456789'})
        with self.assertRaises(QWebException):
            report_object.render_report(docs.ids, report_name, False)
        docs.update({'vat': '1234567890', 'website': '12345678901'})
        with self.assertRaises(QWebException):
            report_object.render_report(docs.ids, report_name, False)
        docs.update(
            {'website': '1234567890', 'company_registry': '12345678901'})
        with self.assertRaises(QWebException):
            report_object.render_report(docs.ids, report_name, False)
        docs.update({
            'fax': fax,
>>>>>>> [ADD] report_field_length
            'vat': vat,
            'website': website,
            'company_registry': company_registry
        })
