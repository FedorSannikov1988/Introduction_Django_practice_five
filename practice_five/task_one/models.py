from django.db import models
from django.core.validators import RegexValidator, \
                                   MinValueValidator


class TableWithResultsCoinToss(models.Model):
    result_coin_toss = models.CharField(max_length=5)
    time_throw = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'ResultsCoinToss: {self.result_coin_toss}, ' \
               f'data_and_time_throw: {self.time_throw}'

    @staticmethod
    def get_statistics(number_throws: int) -> dict:

        all_coin_toss = \
            TableWithResultsCoinToss.objects.order_by('-id')[:number_throws]

        heads: int = 0
        tails: int = 0
        heads_and_tails: int = 0

        for one_coin_toss in all_coin_toss:
            if one_coin_toss.result_coin_toss == "heads":
                heads += 1
            else:
                tails += 1
            heads_and_tails += 1

        return {"heads": heads/heads_and_tails, "tails": tails/heads_and_tails}


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'Author(' \
               f'name:{self.name}, ' \
               f'surname: {self.surname}, ' \
               f'email: {self.email}, ' \
               f'birthday: {self.birthday}' \
               f')'

    def get_name_and_surname(self):
        name = self.name
        surname = self.surname
        return f'{name} {surname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_publication = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    number_views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f'Article(' \
               f'title:{self.title}, ' \
               f'date_publication:{self.date_publication}, ' \
               f'publish: {self.publish}' \
               f')'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    date_change = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Comment(' \
               f'author:{self.author}, ' \
               f'article:{self.article}, ' \
               f'date creation: {self.date_creation}' \
               f'date change: {self.date_change}' \
               f')'


for_phone_number_validation = \
    RegexValidator(
        regex=r"^[0-9]{3,11}$",
        message="Номер телефона должен быть в длинну "
                "от 3 до 11 символов и состоять только из цифр."
    )


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = \
        models.CharField(validators=[for_phone_number_validation],
                         max_length=11)
    address = models.TextField()
    date_and_time_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Client(' \
               f'name: {self.name}, ' \
               f'email: {self.email}, ' \
               f'phone number: ' \
               f'{self.phone_number}, ' \
               f'address: {self.address}, ' \
               f'date and time registration: ' \
               f'{self.date_and_time_registration}' \
               f')'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=10)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    date_and_time_additions_product = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product(' \
               f'name: {self.name}, ' \
               f'price: {self.price}, ' \
               f'quantity: {self.quantity}, ' \
               f'date and time additions product: ' \
               f'{self.date_and_time_additions_product}' \
               f')'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_amount_order = models.DecimalField(max_digits=20, decimal_places=10)
    date_and_time_placing_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        product_count: int = self.product.count()
        product_list: str = ', '.join(str(product) for product in self.product.all())

        return f'Order(' \
               f'client: {self.client}, ' \
               f'product count: {product_count}, ' \
               f'product list: {product_list}, ' \
               f'total amount order: {self.total_amount_order}, ' \
               f'date and time placing order: ' \
               f'{self.date_and_time_placing_order}' \
               f')'
