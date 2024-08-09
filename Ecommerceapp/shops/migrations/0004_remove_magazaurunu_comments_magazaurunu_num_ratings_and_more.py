# Generated by Django 5.0.6 on 2024-07-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shops", "0003_magazaurunu_comments_magazaurunu_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="magazaurunu",
            name="comments",
        ),
        migrations.AddField(
            model_name="magazaurunu",
            name="num_ratings",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="magazaurunu",
            name="total_rating",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
