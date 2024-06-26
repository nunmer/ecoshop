import traceback
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from core import models, forms

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        products = models.Product.objects.filter(owner_id = user.id)
        context['user'] = user
        context['products'] = products

        return context


def products_list(request, pk):
    category = get_object_or_404(models.Category, pk=pk)
    products = models.Product.objects.filter(category=category)
    return render(request, 'products.html', 
                {
                    'category': category,
                    'products': products,
                })


def add_product(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Save the form data, including the picture file
            product = form.save(commit=False)
            product.quantity = request.POST.get('quantity')  # Retrieve quantity from POST data
            product.owner_id = request.user.id
            product.save()
            return redirect('profile')  # Redirect to the profile page after adding the product
    else:
        form = forms.ProductForm()
    return render(request, 'addproduct.html', {'form': form})


def delete_product(request, pk):
    try:
        models.Product.objects.get(pk=pk).delete()
        
        return redirect('profile')
    except Exception as e:
        return JsonResponse(e, status=401)


def purchase_product(request, pk):
    try:
        product = models.Product.objects.get(pk=pk)
        category = product.category.id
        print(category)

        if product.quantity < 2 or product.quantity == None:
            product.delete()
        else:
            product.quantity = product.quantity - 1
            product.save()
        
        return redirect('/products/' + str(category))
    
    except Exception as e:
        return redirect('/products/' + str(category))
    