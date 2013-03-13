==================
Ventas por tiendas
==================

Este módulo permite gestionar tiendas por usuarios:

* Relaciona tiendas con usuarios.
* Busca, filtra y lista por tienda.

.. warning::  Es importante instalar este módulo antes que se realizen pedidos de
              venta. En caso contrario, deberá un técnico instalar este módulo
              y modificar unos parámetros a la base de datos.

Configuración
-------------

Tiendas
-------

Añadiremos las respectivas tiendas ya sean tiendas físicas o tiendas virtuales o
comercio electrónico. Al dar de alta una tienda introducimos los siguientes campos
por defecto de la tienda:

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

En la pestaña usuarios dispondrá de la información de usuarios disponibles a la tienda.

.. note::  La configuración de ventas por defecto de Tryton queda deshabilitado,
           ya que es reemplazado por la configuración de los parámetros por tienda.

Usuarios
--------

A |menu_user| podrá añadir o agregar a que tiendas pueden crear
pedidos. A parte, dispone del campo en que tienda esta activo en este momento.

.. |menu_user| tryref:: res.menu_user_form/complete_name

Preferencias
------------

Los usuarios pueden cambiar de tienda mediante sus preferencias
(Menú superior/Preferencias) y decidir en que tienda están en este momento
creando/editando pedidos.

.. figure:: images/tryton-sale-shop.png

   Configuración de tiendas en Tryton

Pedidos
-------

En el momento de crear un pedido nuevo, este se le asigna a una tienda. Este campo
es requerido y de solo lectura, por tanto, si un usuario no tiene acceso a ninguna
tienda, no podrá generar pedidos, aunque tenga roles de creación de pedidos.

.. note::  Para crear pedidos de venta a parte de disponer de los grupos
           relacionados a ventas, el usuario deberá pertenecer a una o varias
           tiendas.

Clientes
--------

Al añadir un cliente, los campos por defecto se usará los campos definidos en la
ficha del cliente. En caso contrario, si en el cliente no dispone de estos campos,
usará los campos por defecto de la tienda que estamos en uso.

* Política de facturación
* Política de envío
* Almacén de la tienda

Editar o aprobar pedido
-----------------------

Todos los usuarios pueden acceder a los pedidos, pero solo pueden editar aquellos
pedidos relacionados a la tiendas del usuario.

Módulos de los que depende
==========================

Instalados
----------

.. toctree::
   :maxdepth: 1

   /sale/index
   /sale_price_list/index

Dependencias
------------

* Ventas_
* `Tarifas de venta`_

.. _Ventas: ../sale/index.html
.. _Tarifas de venta: ../sale_price_list/index.html
