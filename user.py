#This file is part sale_shop module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pyson import Not, Bool, Eval, Equal, PYSONEncoder, Date
from trytond.pool import Pool

class User(ModelSQL, ModelView):
    "User"
    _name = "res.user"
    _description = __doc__

    shops = fields.Many2Many('sale.shop-res.user', 'user', 'shop', 'Shops')
    shop = fields.Many2One('sale.shop', 'Shop',
            domain=[('id', 'in', Eval('shops', []))],
            depends=['shops'],
    )
    def __init__(self):
        super(User, self).__init__()
        self._preferences_fields.extend([
            'shop',
            'shops',
        ])

    def write(self, ids, vals):
        return super(User, self).write(ids, vals)

User()
