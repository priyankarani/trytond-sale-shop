#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Sale Shop',
    'name_ca_ES': 'Vendes per botiga',
    'name_es_ES': 'Ventas por tienda',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''This module allows to manage shops by users: 
- Set relationship between shops and users.
- Search, filter and list by shop.''',
    'description_ca_ES': '''Aquest mòdul permet gestionar botigues per usuaris:
 - Relaciona botigues amb usuaris.
 - Cerca, filtra i llista per botiga.''',
    'description_es_ES': '''Este módulo permite gestionar tiendas por usuarios:
 - Relaciona tiendas con usuarios.
 - Busca, filtra y lista por tienda.''',
    'depends': [
        'ir',
        'res',
        'sale_price_list',
    ],
    'xml': [
        'shop.xml',
        'sale.xml',
        'user.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}
