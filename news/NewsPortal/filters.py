from django_filters import FilterSet, ModelChoiceFilter, ChoiceFilter
from .models import Post, Category

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.


class PostFilter(FilterSet):
    postCategory = ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='любая'
    )

    categoryType = ChoiceFilter(
        field_name='categoryType',
        label='Type',
        empty_label='все типы',
        choices=Post.CATEGORY_CHOICES
    )

    author = ChoiceFilter(
        field_name='author',
        label='Author',
        empty_label='все авторы'
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'title': ['icontains'],
            'dateCreation': ['day'],
            'text': ['icontains'],
            'postCategory': ['exact'],
            'categoryType': ['exact'],
            'author': ['exact'],
        }