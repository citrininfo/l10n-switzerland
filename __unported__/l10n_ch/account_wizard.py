# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi. Copyright Camptocamp SA
#    Financial contributors: Hasa SA, Open Net SA,
#                            Prisme Solutions Informatique SA, Quod SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import orm


class WizardMultiChartsAccounts(orm.TransientModel):

    _inherit = 'wizard.multi.charts.accounts'

    def onchange_chart_template_id(self, cr, uid, ids,
                                   chart_template_id=False, context=None):
        if context is None:
            context = {}
        res = super(WizardMultiChartsAccounts,
                    self).onchange_chart_template_id(
                        cr, uid, ids,
                        chart_template_id=chart_template_id,
                        context=context)
        # 0 is evaluated as False in python so we have to do this
        # because original wizard test code_digits value on a float widget
        if chart_template_id:
            chart = self.pool['account.chart.template'].browse(
                cr,
                uid,
                chart_template_id,
                context=context
            )
            if chart.name == "Plan comptable STERCHI":
                res['value']['code_digits'] = 0
        return res
