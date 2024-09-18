from .models import Category

def global_category(request):
    munu_links = Category.objects.all()
    return dict(menu_links=munu_links)