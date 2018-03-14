from django.shortcuts import render, HttpResponse, redirect

def index(request):
    
    #initialize session dictionary list to hold words
    if 'products' not in request.session:
        print "initializing request.session('products')"
        request.session['products'] = []
        # add products to session variable (in lieu of having  a database)
        request.session["products"].append({'prod_id': 1, 'prod_name': "Dojo Tshirt", 'prod_price':19.99})
        request.session["products"].append({'prod_id': 2, 'prod_name': "Dojo Sweater", 'prod_price':29.99})
        request.session["products"].append({'prod_id': 3, 'prod_name': "Dojo Cup", 'prod_price':4.99})
        request.session["products"].append({'prod_id': 4, 'prod_name': "Algorithm Book", 'prod_price':49.99})
        print request.session["products"]

    # Set session as modified to force data updates to be saved.
    #request.session.modified = True

    return render(request, 'amadon/index.html')

def buy(request, prod_id):
    prod_id = int(prod_id)
    prod_qty = int(request.POST["prod_qty"])

    if 'buy_curr' not in request.session:
        print "initializing request.session vars related to purchases"
        request.session['buy_curr'] = 0
        request.session['buy_tot'] = 0
        request.session['buy_cnt'] = 0

    for item in request.session["products"]:
        if item['prod_id'] == prod_id:
            item_price = item['prod_price']
            break

    # found item with prod_id and have item price
    # now adjust session variables related tp purchases
    request.session['buy_curr'] = item_price*prod_qty
    request.session['buy_tot'] += request.session['buy_curr']
    request.session['buy_cnt'] += prod_qty
    #request.session.modified = True

    print request.session['buy_curr'], request.session['buy_tot'], request.session['buy_cnt']

    return redirect(checkout)

def checkout(request):
    return render(request, 'amadon/checkout.html')

def reset(request):
    print "clearing session variables"
    request.session.clear()
    return redirect(index)
