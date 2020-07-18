from django.db import models


# Create your models here.
class StockLocation(models.Model):
    name = models.CharField(max_length=32, verbose_name='Name')
    address_line1 = models.CharField(max_length=64, null=True, blank=True, verbose_name='Address')
    address_line2 = models.CharField(max_length=64, null=True, blank=True, verbose_name='Address')

    class Meta:
        ordering = ['name']
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100, blank=False, help_text='Part name')
    description = models.CharField(max_length=250, blank=True, help_text='Part description')
    keywords = models.CharField(max_length=250, blank=True, help_text='Part keywords to improve visibility in search results')
    default_location = models.ForeignKey(StockLocation, on_delete=models.SET_NULL, blank=True, null=True,
                                         help_text='Where is this item normally stored?',
                                         related_name='default_parts')
    producer = models.CharField(max_length=50, blank=True)
    product_series = models.CharField(max_length=100, blank=True)
    manufacturer_index = models.CharField(max_length=200, blank=True)
    creation_date = models.DateField(auto_now_add=True, editable=False, blank=True, null=True)

    class Meta:
        verbose_name = "Part"
        verbose_name_plural = "Parts"

    def __str__(self):
        return "{n} - {d}".format(n=self.name, d=self.description)


class StockItem(models.Model):
    location = models.ForeignKey(
        StockLocation, on_delete=models.DO_NOTHING,
        verbose_name='Stock Location',
        related_name='stock_items',
        blank=True, null=True,
        help_text='Where is this stock item located?'

    )

    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True,
                                         help_text='Is part need to some project?')

    part = models.ForeignKey(
        Item, on_delete=models.CASCADE,
        verbose_name='Base Part',
        related_name='stock_items', help_text='Base part')

    quantity = models.DecimalField(verbose_name="Stock Quantity", max_digits=15, decimal_places=0, default=1)

    updated = models.DateField(auto_now=True, null=True)
    stocktake_date = models.DateField(blank=True, null=True)
    delete_on_deplete = models.BooleanField(default=True, help_text='Delete this Stock Item when stock is depleted')

    status = models.PositiveIntegerField()

    def __str__(self):
        return self.part.name


