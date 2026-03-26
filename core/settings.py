# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# This tells Django where to look for your original files
STATICFILES_DIRS = [
    BASE_DIR / 'images',
    BASE_DIR / 'assets',
    BASE_DIR / 'documents',
]

# This is where Render will "collect" everything for the web
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Use the simpler WhiteNoise storage to avoid "Manifest" 404 errors
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
