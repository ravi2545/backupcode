from django.db import models

# Create your models here.

class JIRAFIELD(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    field_id = models.CharField(max_length=100, primary_key=True)
    schema_json = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    field_key = models.CharField(max_length=255, blank=True, null=True)
    stable_id = models.CharField(max_length=255, blank=True, null=True)
    is_locked = models.BooleanField(default=False)
    searcherKey = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class GetsiteFields(models.Model):
    site_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.site_name


class CheckStatistics(models.Model):
    model_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()


class IssueTypes(models.Model):
    issue_type_id = models.CharField(max_length=1000, blank=False, null=False)
    issue_type_name = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    issue_json = models.JSONField(blank=True, null=True)

    def __str__(self):
        self.issue_type_name or "Unnamed Issue Type"