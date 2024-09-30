from django.db import models


class BlenderPathProject(models.Model):

    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=60)
    time_save_project = models.DateTimeField()
    path_save_project = models.TextField()

    class Meta:
        db_table = 'blender_path_project'
        ordering = ['time_save_project']
        verbose_name = 'Blender project save path'
        verbose_name_plural = 'Path to save blender projects'
