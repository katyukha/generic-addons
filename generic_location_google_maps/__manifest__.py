{
    'name': "Generic Location (Google Maps)",

    'summary': """
    """,

    'author': "Center of Research & Development",
    'website': "https://crnd.pro",

    'category': 'Generic Location',
    'version': '11.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'generic_location_geolocalize',
        'web_google_maps',
    ],

    # always loaded
    'data': [
        'views/generic_location.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'uninstall_hook': 'uninstall_hook',
}
