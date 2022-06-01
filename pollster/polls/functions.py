# Get database information
def get_db_stats(model,id):
    count = model.__class__.objects.count() # number of table rows
    index = list(model.__class__.objects.values_list('id', flat=True)).index(id) + 1 # row index of id
    info = {
        'count': count,
        'index': index}
    return info
