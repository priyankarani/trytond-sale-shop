#This file is part of Tryton.  The COPYRIGHT file at the top level
#of this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool
from trytond.pyson import Eval, Bool

class Sale(ModelSQL, ModelView):
    'Sale'
    _name = 'sale.sale'
    _description = __doc__
    shop = fields.Many2One('sale.shop', 'Shop', required=True, readonly=True)

    def __init__(self):
        super(Sale, self).__init__()
        self._error_messages.update({
                'edit_sale_by_shop': 'You cannot edit this order because you do not '
                    'have permission to edit edit in this shop.',
            })

    def default_shop(self):
        user_obj = Pool().get('res.user')
        user = user_obj.browse(Transaction().user)
        return user.shop and user.shop.id or False

    def on_change_party(self, values):
        user_obj = Pool().get('res.user')
        shop_obj = Pool().get('sale.shop')
        res = super(Sale, self).on_change_party(values)
        user = user_obj.browse(Transaction().user)
        if user.shop:
            if not res.get('price_list') and res.get('invoice_address'):
                res['price_list.rec_name'] = shop_obj.browse(
                    user.shop.id).price_list.rec_name
            if not res.get('payment_term') and res.get('invoice_address'):
                res['payment_term.rec_name'] = shop_obj.browse(
                    user.shop.id).payment_term.rec_name
        return res

    def default_invoice_method(self):
        user_obj = Pool().get('res.user')
        shop_obj = Pool().get('sale.shop')
        user = user_obj.browse(Transaction().user)
        return user.shop and shop_obj.browse(user.shop.id).sale_invoice_method or 'manual'

    def default_shipment_method(self):
        user_obj = Pool().get('res.user')
        shop_obj = Pool().get('sale.shop')
        user = user_obj.browse(Transaction().user)
        return user.shop and shop_obj.browse(user.shop.id).sale_shipment_method or 'manual'

    def default_warehouse(self):
        user_obj = Pool().get('res.user')
        shop_obj = Pool().get('sale.shop')
        location_obj = Pool().get('stock.location')
        user = user_obj.browse(Transaction().user)
        if user.shop:
            return shop_obj.browse(user.shop.id).warehouse.id
        else:
            location_ids = location_obj.search(self.warehouse.domain)
            if len(location_ids) == 1:
                return location_ids[0]

    def set_reference(self, ids):
        '''
        Rewrite fill the reference field with the sale sequence from sale.shop
        '''
        sequence_obj = Pool().get('ir.sequence')
        config_obj = Pool().get('sale.configuration')
        user_obj = Pool().get('res.user')
        shop_obj = Pool().get('sale.shop')

        user = user_obj.browse(Transaction().user)
        config = config_obj.browse(1)
        sales = self.browse(ids)
        for sale in sales:
            if sale.reference:
                continue
            if user.shop:
                sequence_id = shop_obj.browse(user.shop.id).sale_sequence.id
            else:
                sequence_id = config.sale_sequence.id
            reference = sequence_obj.get_id(sequence_id)
            self.write(sale.id, {
                'reference': reference,
                })

    def write(self, ids, vals):
        '''
        Only edit Sale users available edit in this shop
        '''
        sale_obj = Pool().get('sale.sale')
        user_obj = Pool().get('res.user')
        user = user_obj.browse(Transaction().user)

        shops = [s.id for s in user.shops]
        for sale in sale_obj.browse(ids):
            if not sale.shop.id in shops:
                self.raise_user_error('edit_sale_by_shop')
        res = super(Sale, self).write(ids, vals)
        return res

Sale()
