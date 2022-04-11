SUPERADMIN = 1
OWNER = 2
SELLER = 3
DISTRIBUTOR = 4
CLIENT = 5

USER_TYPES = (
    (SUPERADMIN, 'superadmin'),
    (OWNER, 'owner'),
    (SELLER, 'seller'),
    (DISTRIBUTOR, 'distributor'),
    (CLIENT, 'client'),
)

'''
Main documents
'''
DOCUMENT_TEMPLATE_FILE_ALLOWED_EXTENSIONS = ('.docx', '.pdf', '.png', '.jpg', '.tiff')
# 10 MB
DOCUMENT_TEMPLATE_MAX_FILE_SIZE = 10485760

'''
Images
'''
IMAGE_ALLOWED_EXTENSIONS = ('.jpg', '.png')
# 10 MB
IMAGE_MAX_FILE_SIZE = 10485760
