#:before:sale/sale:title:venta#

Tiendas
=======

La opción de tiendas en los pedidos de venta le permitirá establecer una organización
de tiendas (físicas o virtuales) y usuarios por cada tienda.

A |menu_sale_shop| agregaremos una nueva tienda con la información:

* |shop_name|: Nombre de la tienda
* |shop_users|: Usuarios que tendrán acceso a esta tienda.
* |shop_warehouse|: Almacén principal que opera esta tienda.
* |shop_price_list|: Tarifa de venta para esta tienda.
* |shop_payment_term|: Plazos de pago para esta tienda.
* |shop_sale_sequence|: Numeración que usará los pedidos de esta tienda.
* |shop_sale_invoice_method|: Método de facturación que usará esta tienda.
* |shop_sale_shipment_method|: Métode de envío que usará esta tienda.
* |shop_company|: Empresa de esta tienda.

.. |menu_sale_shop| tryref:: sale_shop.menu_sale_shop/complete_name
.. |shop_name| field:: sale.shop/name
.. |shop_users| field:: sale.shop/users
.. |shop_warehouse| field:: sale.shop/warehouse
.. |shop_price_list| field:: sale.shop/price_list
.. |shop_payment_term| field:: sale.shop/payment_term
.. |shop_sale_sequence| field:: sale.shop/sale_sequence
.. |shop_sale_invoice_method| field:: sale.shop/sale_invoice_method
.. |shop_sale_shipment_method| field:: sale.shop/sale_shipment_method
.. |shop_company| field:: sale.shop/company

#:before:sale/sale:paragraph:el_numero_de_referencia_del_pedido#

Según las preferencias del usuario, se creará un pedido de venta según la tienda
que esté activo en este momento. A la pestaña *Información adicional* dispone
del campo en que tienda está relacionado este pedido de venta. Este campo sólo
es de lectura.

* |sale_shop|: Tienda del pedido de venta
    
.. |sale_shop| field:: sale.sale/shop

#:before:sale/sale:title:lineas_del_pedido_de_venta#

En el momento de crear un nuevo pedido de venta, los valores por defecto son
definidos en la configuración de la tienda y pueden ser modificados en el momento
de generar el pedido de venta.

.. note:: Los pedidos de venta sólo se muestran por las tiendas que el usuario tenga
          acceso. Configure el usuario en que tiendas tiene acceso.
