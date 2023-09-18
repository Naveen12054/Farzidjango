from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from accounts.models import Product,CustomUser,SellerProfile,Category
from main.models import BookCart,Wishlist

User = get_user_model
# Create your views here.
def index(request):
    stdata = Category.objects.filter(status=False)
    return render(request,'index.html',{'stdata': stdata})
def cart(request):
    # Assuming you have the user object for the currently logged-in user
    user_id = request.user.id  # Replace with your user retrieval logic if needed
# Retrieve books in the user's cart
    books_in_cart = BookCart.objects.filter(user_id=user_id)
# Retrieve book details for the books in the cart
    book_details = Product.objects.filter(id__in=books_in_cart.values_list('product_id', flat=True))
    total_price = 0
    #product_id=BookCart.request.get(product_id=product_id)
    st = BookCart.objects.filter(user_id=user_id)
    return render(request,"cart.html",{'cart_books':book_details,'st':st,'total_price':total_price})
def increase_item(request, item_id): 
    try: 
        cart_item = BookCart.objects.get(id=item_id) 
        cart_item.quantity += 1 
        cart_item.save() 
    except BookCart.DoesNotExist: 
        pass  # Handle the case when the item does not exist in the cart 
    return redirect('cart')

def singleview(request):
    return render(request, "singleview.html")
def singleview(request, product_id):
    product = get_object_or_404(Product, id=product_id)
        # Record the user's view
    return render(request, 'singleview.html', {'product': product})
def add_cart(request, bookid2):
    userid=request.user.id
    book = BookCart(
        user_id=userid,
        product_id=bookid2        
    )
    book.save()
    return redirect('cart')
def delete_cart(request, bookid2):
    remove=BookCart.objects.filter(product_id=bookid2)
    remove.delete()
    return redirect('cart')
def wishlist(request):
    # Assuming you have the user object for the currently logged-in user
    user_id = request.user.id  # Replace with your user retrieval logic if needed
# Retrieve books in the user's cart
    books_in_cart = Wishlist.objects.filter(user_id=user_id)
# Retrieve book details for the books in the cart
    book_details = Product.objects.filter(id__in=books_in_cart.values_list('product_id', flat=True))
    return render(request,"wishlist.html",{'cart_books':book_details})

def add_wishlist(request, bookid2):
    userid=request.user.id
    book = Wishlist(
        user_id=userid,
        product_id=bookid2        
    )
    book.save()
    return redirect('wishlist')
def delete_wishlist(request, bookid2):
    remove=Wishlist.objects.filter(product_id=bookid2)
    remove.delete()
def catalog(request):
    stdata = Product.objects.filter(status=False)
    return render(request, "catalog.html", {'stdata': stdata})
from django.shortcuts import render
from .models import Category, Product
##########################################
###############     product_list            to display the category bed     #####################
########################################
def product_list(request):
    # Filter products where the 'category' field is "bed"
    products = Product.objects.filter(category='Bed')
    
    return render(request, "product_list.html", {'products': products})

##################################
####################               product_list            to display the category bed      #############
#################################

def full_list(request):
    # Filter products where the 'category' field is "bed"
    products = Product.objects.filter(category='Sofa')
    products1 = Product.objects.filter(category='Chair')
    products2 = Product.objects.filter(category='Bed')
    products4 = Product.objects.filter(category='Outdoor')
    products3 = Product.objects.all()
    products5 = Product.objects.filter(subcategory='Modular sofas')
    products6 = Product.objects.filter(subcategory='Fabric sofas')
    products8 = Product.objects.filter(subcategory='Chaise longues')
    products7 = Product.objects.filter(subcategory='Recliners')
    products9 = Product.objects.filter(subcategory='Accent Chair')
    products10 = Product.objects.filter(subcategory='Study Chair')
    products11 = Product.objects.filter(subcategory='Club Chair')
    products12 = Product.objects.filter(subcategory='Arm Chairs')
    products13 = Product.objects.filter(subcategory='Divan beds')
    products14 = Product.objects.filter(subcategory='Upholstred beds')
    products15 = Product.objects.filter(subcategory=' Double beds')
    products16 = Product.objects.filter(subcategory=' King beds')
    products17 = Product.objects.filter(subcategory='Swings')
    products18 = Product.objects.filter(subcategory='Loungers')
    products19 = Product.objects.filter(subcategory='Seating')
    products20 = Product.objects.filter(subcategory='Hammocks')









    return render(request, "full_list.html", {'products': products,'products1':products1,'products2':products2,'products3':products3,
                                              'products4':products4,'products5':products5,'products6':products6,'products7':products7,
                                              'products8':products8,'products9':products9,'products10':products10,'products11':products11,
                                              'products12':products12,'products13':products13,'products14':products14,'products15':products15,
                                              'products16':products16,'products17':products17,'products18':products18,'products19':products19,
                                              'products20':products20
                                              })



def custlive(request):
    # Filter products where the 'category' field is "bed"
    products = Product.objects.filter(category='Sofa')
    products1 = Product.objects.filter(category='Chair')
    products2 = Product.objects.filter(category='Bed')
    products4 = Product.objects.filter(category='Outdoor')
    products3 = Product.objects.all()
    products5 = Category.objects.all()
    return render(request, "custlive.html", {'products': products,'products1':products1,
                                             'products2':products2,'products3':products3,'products4':products4,
                                             'products5':products5,})


def separate(request):
    stdata = Product.objects.filter(status=False,)
    stdata1 = Category.objects.all()
    return render(request, "separate.html", {'stdata': stdata,'stdata1': stdata1})

def display_all_objects(request):
    objects = CustomUser.objects.all()  # Retrieve all objects from YourModel
    seller_profiles = SellerProfile.objects.all()  # Retrieve all SellerProfile objects

    context = {
        'objects': objects,
        'seller_profiles': seller_profiles,  # Add SellerProfile data to the context
    }

    return render(request, 'display_all_objects.html', context)
# def users(request):
#     stdata = CustomUser.objects.all()
#     return render(request, "users.html", {'stdata': stdata})
#
def inactiveseller(request, stid2):
    dele=CustomUser.objects.get(id=stid2)
    if dele.is_active == False: 
        dele.is_active=True
    else:
        dele.is_active=False
    dele.save()
    return redirect('display_all_objects')

