from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import Category, Product
from .forms import CategoryForm, ProductForm

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def all_category(request):
    categoryes = Category.objects.all()
    return render(request, "categoryes.html", {"categoryes": categoryes})

def all_product(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def category_by_id_get(request, id):
    category = Category.objects.filter(categoryId=id)
    print(category)
    products = Product.objects.filter(category_id=id)
    return render(request, "categoryesById.html", {"category": category[0], "products": products})

def category_by_id_delete(request):
    if request.method == "POST":
        Category.objects.filter(category_id=request.POST["categoryId"]).delete()
        return HttpResponse("Delete!")
    else:
        form = CategoryForm()
    return render(request, "categoryDelete.html", {"form": form})

def category_by_id_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return HttpResponse("Created!")
    else:
        form = CategoryForm()
    return render(request, "categoryCreate.html", {"form": form})

def product_by_id_get(request, id):
    productObj = Product.objects.filter(category_id=id)
    return HttpResponse(productObj)

def product_by_id_delete(request, id):
    Product.objects.filter(productId=id).delete()
    return HttpResponse("Deleted!")

def product_by_id_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    return HttpResponseRedirect("/products")
