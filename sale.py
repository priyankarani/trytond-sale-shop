#This file is part sale_shop module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta

class Sale:
    'Sale'
    __name__ = 'sale.sale'
    shop = fields.Many2One('sale.shop', 'Shop', required=True, readonly=True)

    @classmethod
    def __setup__(cls):
        super(Sale, cls).__setup__()
        cls._error_messages.update({
                'not_sale_shop': 'What shop would like to sell? Go to preferences',
                'edit_sale_by_shop': 'You cannot edit this order because you do not '
                    'have permission to edit edit in this shop.',
            })

    @staticmethod
    def default_shop():
        User = Pool().get('res.user')
        user = User.browse([Transaction().user])[0]

        return user.shop and user.shop.id or False

    def on_change_party(self):
        User = Pool().get('res.user')
        Shop = Pool().get('sale.shop')
        res = super(Sale, self).on_change_party()
        user = User.browse([Transaction().user])[0]
        if user.shop:
            if not res.get('price_list') and res.get('invoice_address'):
                res['price_list.rec_name'] = Shop.browse([
                    user.shop])[0].price_list.rec_name
            if not res.get('payment_term') and res.get('invoice_address'):
                res['payment_term.rec_name'] = Shop.browse([
                    user.shop])[0].payment_term.rec_name
        return res

    @staticmethod
    def default_invoice_method():
        User = Pool().get('res.user')
        user = User.browse([Transaction().user])[0]
        return user.shop and user.shop.sale_invoice_method or 'manual'

    @staticmethod
    def default_shipment_method():
        User = Pool().get('res.user')
        user = User.browse([Transaction().user])[0]
        return user.shop and user.shop.sale_shipment_method or 'manual'

    @staticmethod
    def default_warehouse():
        User = Pool().get('res.user')
        user = User.browse([Transaction().user])[0]
        if user.shop:
            return user.shop.warehouse.id
        else:
            Location = Pool().get('stock.location')
            return Location.search([('type', '=', 'warehouse')], limit=1)[0].id

    @classmethod
    def set_reference(cls, records):
        '''
        Rewrite fill the reference field with the sale sequence from sale.shop
        '''
        Sequence = Pool().get('ir.sequence')
        Config = Pool().get('sale.configuration')
        User = Pool().get('res.user')
        Shop = Pool().get('sale.shop')

        user = User.browse([Transaction().user])[0]
        config = Config.browse(1)[0]
        sales = records
        for sale in sales:
            if sale.reference:
                continue
            if user.shop:
                sequence_id = Shop.browse([user.shop.id])[0].sale_sequence.id
            else:
                sequence_id = config.sale_sequence.id
            reference = Sequence.get_id(sequence_id)
            cls.write(sale.id, {
                'reference': reference,
                })

    @classmethod
    def create(cls, vals):
        User = Pool().get('res.user')
        user = User.browse([Transaction().user])[0]
        
        if not user.shop:
            cls.raise_user_error('not_sale_shop')

        vals = vals.copy()
        vals['shop'] = user.shop.id
        return super(Sale, cls).create(vals)

    @classmethod
    def write(cls, sales, vals):
        '''
        Only edit Sale users available edit in this shop
        '''
        User = Pool().get('res.user')
        user = User.browse([Transaction().user])[0]
        print user.shops
        shops = [s.id for s in user.shops]
        for sale in sales:
            if not sale.shop.id in shops:
                cls.raise_user_error('edit_sale_by_shop')
        res = super(Sale, cls).write(sales, vals)
        return res
