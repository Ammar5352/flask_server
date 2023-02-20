ALLOWED_EXTENSIONS=['png','jpg','jpeg','jfif']

def  file_valid(f):
    return '.' in f and \
    f.rsplit('.',1)[1] in ALLOWED_EXTENSIONS