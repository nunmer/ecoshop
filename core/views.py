from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from core import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user'] = user
        return context


def products_list(request, pk):
    category = get_object_or_404(models.Category, pk=pk)
    products = models.Product.objects.filter(category=category)
    return render(request, 'products.html', 
                {
                    'category': category,
                    'products': products,
                })