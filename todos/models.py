from django.db import models


class GoWishUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.id} - {self.name}"


class WishList(models.Model):
    owner = models.ForeignKey(
        GoWishUser, on_delete=models.CASCADE, related_name="wishlists"
    )


class Wish(models.Model):
    wishlist = models.ForeignKey(
        WishList, on_delete=models.CASCADE, related_name="wishes"
    )
    url = models.CharField(max_length=500, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    title = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] + ("..." if len(self.text) > 50 else "")


class ImportanceChoices(models.TextChoices):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)
    importance = models.CharField(
        choices=ImportanceChoices.choices, null=True, blank=True
    )

    owner = models.ForeignKey(
        GoWishUser,
        on_delete=models.CASCADE,
        related_name="todos",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.id} - {self.title}"
