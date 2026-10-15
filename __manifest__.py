{
    'name' : 'GPSMap - Engine',
    'price' : '49.0',
    'currency' : 'EUR',
    'license' : 'LGPL-3',
    'images': ['static/description/map_online.png'],

    'author': "SolesGPS :: Eduardo Vizcaino",
    'category': 'Human Resources/Fleet GPS',
    "version": "16.0.0.0.0",
    'website' : 'https://solesgps.com',
    'summary' : 'Sends commands to the GPS, including engine shutdown.',
    'depends': [
        'gpsmap',
    ],
    'data': [
        # VIEW
        'views/fleet_vehicle.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'gpsmap_engine/static/xml/*.xml',
        ],        
        'web.assets_qweb': [
            'gpsmap_engine/static/xml/*.xml',
        ],        
    },    
    'installable': True,
    'application': False,
}