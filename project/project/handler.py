from django.conf import settings

class Database:
    db = settings.db
    collection = db['data-pipeline']