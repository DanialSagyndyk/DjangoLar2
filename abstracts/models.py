# Django Modules
from django.db import models
from django.utils import timezone


#Django Soft Delete Abstract Model

class SoftDeleteQuery(models.QuerySet):
    def delete(self):
        return super().update(is_deleted=True, deleted_at=models.timezone.Now())

    def hard_delete(self):
        return super().delete()

    def alive(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)

    def all_with_deleted(self):
        return self.all()

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuery(self.model, using=self._db).filter(is_deleted=False)

    def all_with_deleted(self):
        return SoftDeleteQuery(self.model, using=self._db)

    def deleted(self):
        return self.get_queryset().deleted()

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = SoftDeleteManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
