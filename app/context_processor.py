from app.models import Category

def category_list(request):
    data = {
        'categories': Category.objects.all(),
    }
    return data
