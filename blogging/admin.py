from django.contrib import admin

from blogging.models import Post, Category


@admin.register(Category)
class CatagoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    exclude = ("posts",)
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
        ]
    