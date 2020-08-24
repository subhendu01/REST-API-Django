from django.db import models

#ORM - Object Relational Mapper

class JobApplicant(models.Model):
    first_name = models.CharField(max_length=40, blank=False, default='')
    last_name = models.CharField(max_length=40, blank=False, default='')
    mob_num = models.CharField(max_length=16, blank=False, default='')
    job_title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    immediate_join = models.BooleanField(default=False)

    # specific table name
    class Meta:
        db_table = 'Job Applicant'

    def __str__(self):
        return self.first_name