{
    'name': "Generic Location",

    'summary': """
        Allows you to make an abstract description of the
        objects location relative to the general location
        (for example: house3 -> office5 -> room2 -> table5)""",

    'author': "Center of Research and Development",
    'website': "https://crnd.pro",

    'category': 'Generic Location',
    'version': '11.0.1.1.11',

    # any module necessary for this one to work correctly
    'depends': [
        'generic_mixin',
        'mail',
    ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/generic_location.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo_location.xml'
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    "license": "LGPL-3",
}
