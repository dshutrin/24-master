from .models import *


def search_by_filters(request, products):
    data = {}

    if request.POST['find']:
        data['find'] = request.POST['find']
    if request.POST['height_start'].replace('.', '').isdigit():
        data['height_start'] = float(request.POST['height_start'])
    if request.POST['height_end'].replace('.', '').isdigit():
        data['height_end'] = float(request.POST['height_end'])
    if request.POST['width_start'].replace('.', '').isdigit():
        data['width_start'] = float(request.POST['width_start'])
    if request.POST['width_end'].replace('.', '').isdigit():
        data['width_end'] = float(request.POST['width_end'])
    if request.POST['len_start'].replace('.', '').isdigit():
        data['len_start'] = float(request.POST['len_start'])
    if request.POST['find'].replace('.', '').isdigit():
        data['len_end'] = float(request.POST['len_end'])
    if request.POST['price_start'].replace('.', '').isdigit():
        data['price_start'] = float(request.POST['price_start'])
    if request.POST['price_end'].replace('.', '').isdigit():
        data['price_end'] = float(request.POST['price_end'])
    if request.POST['weight_start'].replace('.', '').isdigit():
        data['weight_start'] = float(request.POST['weight_start'])
    if request.POST['weight_end'].replace('.', '').isdigit():
        data['weight_end'] = float(request.POST['weight_end'])
    if request.POST['beton_start'].replace('.', '').isdigit():
        data['beton_start'] = float(request.POST['beton_start'])
    if request.POST['beton_end'].replace('.', '').isdigit():
        data['beton_end'] = float(request.POST['beton_end'])

    for param in data:
        if param == 'find':
            if data['find']:
                products = [
                    x for x in products
                    if data[param].lower() in x.name.lower() or data[param].lower() in x.product_code.lower()
                       or data[param].lower() in [y.tag.name.lower() for y in ProductTag.objects.filter(product=x)]
                ]

        if param == 'height_start':
            products = [x for x in products if x.height]
            products = [x for x in products if x.height >= data[param]]
        if param == 'height_end':
            products = [x for x in products if x.height]
            products = [x for x in products if x.height <= data[param]]
        if param == 'width_start':
            products = [x for x in products if x.width]
            products = [x for x in products if x.width >= data[param]]
        if param == 'width_end':
            products = [x for x in products if x.width]
            products = [x for x in products if x.width <= data[param]]
        if param == 'len_start':
            products = [x for x in products if x.length]
            products = [x for x in products if x.length >= data[param]]
        if param == 'len_end':
            products = [x for x in products if x.length]
            products = [x for x in products if x.length <= data[param]]
        if param == 'price_start':
            products = [x for x in products if x.price]
            products = [x for x in products if x.price >= data[param]]
        if param == 'price_end':
            products = [x for x in products if x.price]
            products = [x for x in products if x.price <= data[param]]
        if param == 'weight_start':
            products = [x for x in products if x.weight]
            products = [x for x in products if x.weight >= data[param]]
        if param == 'weight_end':
            products = [x for x in products if x.weight]
            products = [x for x in products if x.weight <= data[param]]
        if param == 'beton_start':
            products = [x for x in products if x.concrete]
            products = [x for x in products if x.concrete >= data[param]]
        if param == 'beton_end':
            products = [x for x in products if x.concrete]
            products = [x for x in products if x.concrete <= data[param]]

    return products
