from django.db import models


class MetaCard(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AbstractCard(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class LianaCard(AbstractCard, MetaCard):
    metacard_ptr = models.OneToOneField(MetaCard, on_delete=models.CASCADE, parent_link=True, primary_key=True, related_name='liana')


class FoxxCard(AbstractCard, MetaCard):
    metacard_ptr = models.OneToOneField(MetaCard, on_delete=models.CASCADE, parent_link=True, primary_key=True, related_name='foxx')


class FoxxDisplay(models.Model):
    card = models.OneToOneField(FoxxCard, on_delete=models.CASCADE)
