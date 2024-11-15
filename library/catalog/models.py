from django.db import models

class Person(models.Model):
    first_name = models.CharField('Имя', max_length=128)
    second_name = models.CharField('Фамилия', max_length=128)
    last_name = models.CharField('Отчество', max_length=128, blank=True)

    description = models.TextField('Описание', blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.last_name}"

    class Meta:
        abstract = True


class Genre(models.Model):
    genre = models.CharField('Жанр', max_length=128)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'Жанры'


class Author(Person):
    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    title = models.CharField('Название', max_length=256)
    author = models.ForeignKey(
        Author,
        on_delete=models.RESTRICT,
        verbose_name="Автор"
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.RESTRICT,
        verbose_name="Жанр",
        blank=True
    )
    description = models.TextField('Аннотация', blank=True)

    icon = models.ImageField('Фото', upload_to='icons', blank=True)
    published_date = models.DateField('Дата публикации')

    fb2 = models.FileField('Файл fb2', upload_to='fb2', blank=True)
    epub = models.FileField('Файл epub', upload_to='epub', blank=True)
    mobi = models.FileField('Файл mobi', upload_to='mobi', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'Книги'


class Translator(Person):    
    class Meta:
        verbose_name = 'переводчик'
        verbose_name_plural = 'Переводчики'


class Translation(models.Model):
    translator = models.ForeignKey(
        Translator,
        on_delete=models.CASCADE,
        verbose_name="Переводчик"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книга"
    )

    def __str__(self):
        return f"{self.translator} - {self.book}"

    class Meta:
        verbose_name = 'перевод'
        verbose_name_plural = 'Переводы'
