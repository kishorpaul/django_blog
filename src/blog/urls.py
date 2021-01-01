from django.urls import path
from blog.views import(
	create_blog_view,
	detailed_blog_view,
	edit_blog_view,
)

app_name = 'blog'

urlpatterns = [
	path('create/', create_blog_view, name="create"),
	path('<slug>/', detailed_blog_view, name="detail"),
	path('<slug>/edit', edit_blog_view, name="edit"),
]