from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from django.urls import reverse

# from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType model Definition"""

    class Meta:
        verbose_name = "Room Type"

    pass


class Amenity(AbstractItem):
    """ Amenity model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"

    pass


class Facility(AbstractItem):
    """ Facility model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"

    pass


class HouseRole(AbstractItem):
    """ HouseRole model Definition """

    class Meta:
        verbose_name = "House Rule"

    pass


class Photo(core_models.TimeStampedModel):
    """Photo Model definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)
    # can do use String
    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """ Room Model definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRole", related_name="rooms", blank=True)

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews))
        return 0

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})