{
    "name": "Generic Condition - Marketing",
    "version": "11.0.0.0.3",
    "author": "Center of Research & Development",
    "website": "https://crnd.pro",
    "license": "LGPL-3",
    "summary": "Generic Conditions (Integration with marketing campaigns)",
    'category': 'Marketing',
    'depends': [
        'generic_condition',
        'marketing_campaign',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/marketing_campaign_view.xml',
        # 'wizard/test_condition_view.xml',
    ],
    'installable': False,
    'auto_install': True,
}
