# Generated by Django 4.2.13 on 2024-09-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0006_delete_menu_image_remove_payment_amount_order_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="price",
            name="selling_price",
        ),
        migrations.AlterField(
            model_name="nutrients",
            name="calories",
            field=models.DecimalField(
                decimal_places=3, max_digits=7, null=True, verbose_name="에너지 (kcal)"
            ),
        ),
        migrations.AlterField(
            model_name="nutrients",
            name="carbohydrate",
            field=models.DecimalField(
                decimal_places=3, max_digits=7, null=True, verbose_name="탄수화물 (g)"
            ),
        ),
        migrations.AlterField(
            model_name="nutrients",
            name="fat",
            field=models.DecimalField(
                decimal_places=3, max_digits=7, null=True, verbose_name="지방 (g)"
            ),
        ),
        migrations.AlterField(
            model_name="nutrients",
            name="protein",
            field=models.DecimalField(
                decimal_places=3, max_digits=7, null=True, verbose_name="단백질 (g)"
            ),
        ),
        migrations.AlterField(
            model_name="nutrients",
            name="sodium",
            field=models.DecimalField(
                decimal_places=3, max_digits=7, null=True, verbose_name="나트륨 (mg)"
            ),
        ),
        migrations.AlterField(
            model_name="nutrients",
            name="sugar",
            field=models.DecimalField(
                decimal_places=3, max_digits=7, null=True, verbose_name="총 당류 (g)"
            ),
        ),
        migrations.AlterField(
            model_name="nutrients",
            name="total_fatty_acids",
            field=models.DecimalField(
                decimal_places=3,
                max_digits=7,
                null=True,
                verbose_name="총 포화 지방산 (g)",
            ),
        ),
        migrations.AlterField(
            model_name="nutrients",
            name="trans_fatty_acid",
            field=models.DecimalField(
                decimal_places=3,
                max_digits=7,
                null=True,
                verbose_name="트랜스 지방산 (g)",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="price",
            field=models.IntegerField(verbose_name="소비자가"),
        ),
    ]