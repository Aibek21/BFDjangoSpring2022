def book_image_directory_path(instance, filename):
    return f'books//{instance.id}/images/{filename}'


def book_file_directory_path(instance, filename):
    return f'books//{instance.id}/files/{filename}'

# def book_image_delete(filename):
#     product_image_path = os.path.abspath(os.path.join(filename.path, '../..'))
#     shutil.rmtree(product_image_path)
