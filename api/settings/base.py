import os

from api.settings import constants

SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
}

POOL_OF_RAMOS = {
    'report': [
        constants.FAKE_REPORT_BACKEND,
        constants.FAKE_REPORT_ERROR_BACKEND
    ]
}

# DEFAULT BACKENDS
DEFAULT_REPORT_BACKEND = os.getenv('DEFAULT_REPORT_BACKEND', 'fake-report')

CACHE = {
    'default': {
        'cache': 'aiocache.SimpleMemoryCache',
        'serializer': {
            'class': 'aiocache.serializers.JsonSerializer'
        }
    }
}
