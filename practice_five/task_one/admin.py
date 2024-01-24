from django.contrib import admin
from task_one.models import TableWithResultsCoinToss, \
                            Author, Article, Comment, \
                            Client, Product, Order


@admin.action(description="Сбросить количество просмотров в ноль")
def reset_number_views(modeladmin, request, queryset):
    queryset.update(number_views=0)


@admin.action(description="Сделать статьи(-ю) не публикованной")
def reset_publish(modeladmin, request, queryset):
    queryset.update(publish=False)


class AuthorAdmin(admin.ModelAdmin):

    list_display = ['name', 'surname', 'birthday', 'email']
    ordering = ['birthday']
    list_filter = ['name', 'surname', 'birthday', 'email']
    search_fields = ['name']
    search_help_text = 'Поиск по полю name'

    #fields = ['name', 'surname', 'email', 'biography', 'birthday']
    readonly_fields = ['birthday']
    fieldsets = [
        (
            'Имя',
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Фамилия',
            {
                'classes': ['wide'],
                'fields': ['surname'],
            },
        ),
        (
            'Электронная почта',
            {
                'classes': ['wide'],
                'fields': ['email'],
            },
        ),
        (
            'Биография',
            {
                'classes': ['collapse'],
                'fields': ['biography'],
            },
        ),
        (
            'Дата Рождения',
            {
                'description': 'Дата Рождения - Не Изменяется !',
                'classes': ['date_added'],
                'fields': ['birthday'],
            },
        ),
    ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'get_author_name', 'number_views', 'publish']
    list_filter = ['title', 'category', 'publish']
    search_fields = ['title']
    search_help_text = 'Поиск по полю title'
    actions = [reset_number_views, reset_publish]

    #fields = ['title', 'content', 'date_publication', 'author', 'category', 'number_views', 'publish']
    readonly_fields = ['date_publication']
    fieldsets = [
        (
            'Заголовок',
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Содержание',
            {
                'classes': ['collapse'],
                'fields': ['content'],
            },
        ),
        (
            'Дата публикации',
            {
                'description': 'Дата публикации - Не Изменяется !',
                'classes': ['date_added'],
                'fields': ['date_publication'],
            },
        ),
        (
            'Автор статьи',
            {
                'classes': ['wide'],
                'fields': ['author'],
            },
        ),
        (
            'Категории',
            {
                'classes': ['wide'],
                'fields': ['category'],
            },
        ),
        (
            'Количество просмотров',
            {
                'classes': ['wide'],
                'fields': ['number_views'],
            },
        ),
        (
            'Опубликована или нет',
            {
                'classes': ['wide'],
                'fields': ['publish'],
            },
        ),
    ]

    def get_author_name(self, obj):
        return obj.author.name


class CommentAdmin(admin.ModelAdmin):
    list_display = ['get_article_title', 'get_author_name', 'date_creation', 'date_change']
    ordering = ['-date_creation', '-date_change']
    list_filter = ['date_creation', 'date_change']

    #fields = ['author', 'article', 'comment', 'date_creation', 'date_change']
    readonly_fields = ['date_creation', 'date_change']
    fieldsets = [
        (
            'Автор',
            {
                'classes': ['wide'],
                'fields': ['author'],
            },
        ),
        (
            'Статьи',
            {
                'classes': ['wide'],
                'fields': ['article'],
            },
        ),
        (
            'Комментарии',
            {
                'classes': ['collapse'],
                'fields': ['comment'],
            },
        ),
        (
            'Дата создания',
            {
                'description': 'Дата создания - Не Изменяется !',
                'classes': ['date_added'],
                'fields': ['date_creation'],
            },
        ),
        (
            'Дата изминения',
            {
                'description': 'Дата изминения - Не Изменяется !',
                'classes': ['date_added'],
                'fields': ['date_change'],
            },
        ),
    ]

    def get_author_name(self, obj):
        return obj.author.name

    def get_article_title(self, obj):
        return obj.article.title


admin.site.register(TableWithResultsCoinToss)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
