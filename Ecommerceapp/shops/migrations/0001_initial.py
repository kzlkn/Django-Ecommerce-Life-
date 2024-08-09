# Generated by Django 5.0.6 on 2024-06-25 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UrunKategorisi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("etiket", models.CharField(db_index=True, max_length=255)),
                ("yol_adi", models.SlugField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "Ürün Kategorisi",
                "verbose_name_plural": "Ürün Kategorileri",
                "ordering": ("etiket",),
            },
        ),
        migrations.CreateModel(
            name="MagazaUrunu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("urun_adi", models.CharField(max_length=300)),
                ("uretici", models.CharField(default="Generic", max_length=300)),
                ("urun_tanimi", models.TextField(blank=True)),
                ("yol_kodu", models.SlugField(max_length=300)),
                ("fiyat", models.DecimalField(decimal_places=2, max_digits=6)),
                ("urun_resmi", models.ImageField(upload_to="urun_fotograflari/")),
                ("stok_miktari", models.PositiveIntegerField()),
                ("stokta_var", models.BooleanField(default=True)),
                (
                    "kategori",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="urunler",
                        to="shops.urunkategorisi",
                    ),
                ),
            ],
            options={
                "verbose_name": "Magaza Urunu",
                "verbose_name_plural": "Magaza Urunleri",
                "ordering": ("urun_adi",),
            },
        ),
    ]
