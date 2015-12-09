from app.models import Category, Post

def category_list(request):
    data = {
        'categories': Category.objects.all(),
    }
    return data

def page_list(request):
    data = {
        'pages': Post.objects.filter(is_page=True),
    }
    return data
