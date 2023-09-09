from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login as auth_login ,authenticate, logout
from django.shortcuts import render, redirect

from django.contrib  import messages,auth
from .models import Category, CustomUser, Product, SellerProfile,UserProfile
# from accounts.backends import EmailBackend
from django.contrib.auth import get_user_model
#from .forms import UserForm, ServiceForm 

User = get_user_model()



def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        print(email)  # Print the email for debugging
        print(password)  # Print the password for debugging

        if email and password:
            user = authenticate(request, email=email, password=password)
            print("Authenticated user:", user)  # Print the user for debugging
            if user is not None:
                auth_login(request, user)
                print("User authenticated:", user.email, user.role)
                return redirect('http://127.0.0.1:8000/')
            else:
                error_message = "Invalid login credentials."
                return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = "Please fill out all fields."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request,'login.html')
                  
def register(request):
    if request.method == 'POST':
        name1 = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('pass', None)
        role = User.CUSTOMER
        print(email)

        if name1 and email and role and password:
            if User.objects.filter(email=email).exists():
                error_message = "Email is already registered."
                return render(request, 'login.html', {'error_message': error_message})
            
            else:
                user = User(name=name1, email=email, role=role)
                user.set_password(password)  # Set the password securely
                user.save()
                user_profile=UserProfile(user=user)
                user_profile.save()
                return redirect('login')  
            
    return render(request, 'register.html')
def profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        # Update user fields
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.phone_no = request.POST.get('phone_no')
        user.save()

        # Update user profile fields
        user_profile.country = request.POST.get('country')
        user_profile.state = request.POST.get('state')
        user_profile.city = request.POST.get('city')
        user_profile.district = request.POST.get('district')
        
        user_profile.aphone_no = request.POST.get('aphone_no')
        user_profile.phone_no = request.POST.get('phone_no')
        user_profile.addressline1 = request.POST.get('addressline1')
        user_profile.addressline2 = request.POST.get('addressline2')
        user_profile.pin_code = request.POST.get('pin_code')
        
        user_profile.save()

        return redirect('profile') 
    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)

#seller profile
def sellerprofile(request):
    user = request.user
    user_profile = SellerProfile.objects.get(user=user)
    if request.method == 'POST':
        # Update user fields
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()

        # Update user profile fields
        user_profile.country = request.POST.get('country')
        user_profile.state = request.POST.get('state')
        user_profile.city = request.POST.get('city')
        user_profile.district = request.POST.get('district')
        user_profile.aphone_no = request.POST.get('aphone_no')
        user_profile.map = request.POST.get('map')
        user_profile.gstno = request.POST.get('gstno')
        user_profile.panno = request.POST.get('panno')
        user_profile.ownername = request.POST.get('ownername')
        user_profile.phone_no = request.POST.get('phone_no')
        user_profile.addressline1 = request.POST.get('addressline1')
        user_profile.addressline2 = request.POST.get('addressline2')
        user_profile.pin_code = request.POST.get('pin_code')
        
        user_profile.save()

        return redirect('index') 
    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'sellerprofile.html', context)

def seller(request):
    if request.method == 'POST':
        name1 = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('pass', None)
        role = User.SELLER
        print(email)

        if name1 and email and role and password:
            if User.objects.filter(email=email).exists():
                error_message = "Email is already registered."
                return render(request, 'login.html', {'error_message': error_message})
            
            else:
                user = User(name=name1, email=email, role=role)
                user.set_password(password)  # Set the password securely
                user.save()
                user_profile = SellerProfile(user=user)
                user_profile.save()
                return redirect('login')  
            
    return render(request, 'seller.html')
def userLogout(request):
    logout(request)
    return redirect('/')
def admindashboard(request):
    return render(request, 'admindashboard.html')




def category(request):
    stdata = Category.objects.filter(status=False)
    return render(request, "category.html", {'stdata': stdata})
def update(request, stid2):
    stid =get_object_or_404(Category,id=stid2) 
    #Category.objects.get(id=stid2)
    stid1=Category.objects.filter(id=stid2)
    if request.method == 'POST':
        stid.category_name = request.POST.get('category_name')
        stid.subcategory1_name = request.POST.get('subcategory1_name')
        stid.subcategory2_name = request.POST.get('subcategory2_name')
        stid.subcategory3_name = request.POST.get('subcategory3_name')
        stid.subcategory4_name = request.POST.get('subcategory4_name')
        stid.category_image = request.POST.get('category_image')

        if 'category_image' in request.FILES:
            stid.category_image = request.FILES['category_image']

        stid.save()
        return redirect("category")

    return render(request, 'addcategory.html', {'station': stid1})
def newcategory(request):

    error_message = ''
    new_category = Category.objects.all()

    if request.method == 'POST':
        # Create a new Category instance and assign values
        new_category = Category()
        new_category.category_name = request.POST.get('category_name')
        new_category.subcategory3_name = request.POST.get('subcategory3_name')
        new_category.subcategory1_name = request.POST.get('subcategory1_name')
        new_category.subcategory2_name = request.POST.get('subcategory2_name')
        new_category.subcategory4_name = request.POST.get('subcategory4_name')
        new_category.category_image = request.FILES.get('category_image')
        new_category.save()
        
        return redirect("category")
    
    context = {
        'new_category': new_category
        
        
    }
    return render(request, "newcategory.html", context)
#######################################################
#To add Product 
def sellerindex(request):
    selected_category = request.GET.get('category')
    stdata = Category.objects.all()
    user = request.user
    userid = user.id
    if request.method == 'POST':
        # Create a new Category instance and assign values
        newproduct = Product(
        product_name = request.POST.get('product_name'),
        brand_name = request.POST.get('brand_name'),
        product_description = request.POST.get('product_description'),
        material_description = request.POST.get('material_description'),
        price = request.POST.get('price'),
        quantity = request.POST.get('quantity'),
        category = request.POST.get('category'),
        subcategory = request.POST.get('subcategory'),
        product_images1 = request.FILES.get('product_images1'),
        product_images2 = request.FILES.get('product_images2'),
        product_images3 = request.FILES.get('product_images3'),
        product_images4 = request.FILES.get('product_images4'),
        user_id=userid
        )
        newproduct.save()   
        
        return redirect("product")
    return render(request, "sellerindex.html",{'stdata': stdata})
#######################################################
#view the products
def product(request):
    user_id=request.user.id
    stdata = Product.objects.filter(user_id=user_id,status=False)
    return render(request, "product.html", {'stdata': stdata})
######################################################
def deletecategory(request, stid2):
    dele=Category.objects.get(id=stid2)
    dele.status=True
    dele.save()
    return redirect('category')

def deleteproduct(request, stid2):
    dele=Product.objects.get(id=stid2)
    dele.status=True
    dele.save()
    return redirect('product')

def sellerpage(request):
    return render(request, "sellerpage.html")

