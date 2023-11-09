# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_group = fields.Boolean(
        string="Grupo",
        default=False,
    )
