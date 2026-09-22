from django.db import models

# Create your models here.


class SiteInfo(models.Model):
    site_name = models.CharField(max_length=100, default="Site Name")
    site_description = models.TextField(blank=True)
    site_logo = models.ImageField(upload_to="site_logos/", blank=True)
    site_favicon = models.ImageField(
        upload_to="site_favicons/",
        blank=True,
    )

    def __str__(self):
        return self.site_name
