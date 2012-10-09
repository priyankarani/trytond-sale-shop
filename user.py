#This file is part sale_shop module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval
from trytond.pool import Pool, PoolMeta

__all__ = ['User']
__metaclass__ = PoolMeta

class User:
    "User"
    __name__ = "res.user"

    shops = fields.Many2Many('sale.shop-res.user', 'user', 'shop', 'Shops')
    shop = fields.Many2One('sale.shop', 'Shop',
            domain=[('id', 'in', Eval('shops', []))],
            depends=['shops'],
    )

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()
        cls._preferences_fields.extend([
            'shop',
            'shops',
        ])

    @classmethod
    def write(cls, users, vals):
        return super(User, cls).write(users, vals)

