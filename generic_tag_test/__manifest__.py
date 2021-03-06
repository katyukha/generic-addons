{
    "name": "Generic Tag - Test",
    "version": "11.0.1.0.8",
    "author": "Center of Research and Development",
    "website": "https://crnd.pro",
    "license": "LGPL-3",
    "summary": "Generic Tag - Tests (do not install manualy)",
    'category': 'Technical Settings',
    'depends': [
        'generic_tag',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/demo.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
