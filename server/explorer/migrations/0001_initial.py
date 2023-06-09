# Generated by Django 3.2.15 on 2022-08-31 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('chainwork', models.CharField(blank=True, max_length=32, null=True)),
                ('difficulty', models.FloatField(blank=True, null=True)),
                ('hash', models.CharField(db_index=True, max_length=128)),
                ('height', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('prev', models.CharField(max_length=128)),
                ('fee', models.FloatField(blank=True, null=True)),
                ('rate_btc', models.CharField(blank=True, max_length=32, null=True)),
                ('rate_usd', models.CharField(blank=True, max_length=32, null=True)),
                ('subsidy', models.BigIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Bot_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(blank=True, max_length=64, null=True)),
                ('height', models.IntegerField()),
                ('sid', models.CharField(blank=True, max_length=64, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('subtype', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Forks_event_detection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Max_privacy_withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=16)),
                ('per_day', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rollback_reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height_from', models.PositiveIntegerField()),
                ('height_to', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Swap_stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc', models.CharField(max_length=16)),
                ('dash', models.CharField(max_length=16)),
                ('doge', models.CharField(max_length=16)),
                ('ltc', models.CharField(max_length=16)),
                ('qtum', models.CharField(max_length=16)),
                ('wbtc', models.CharField(max_length=16)),
                ('usdt', models.CharField(max_length=16)),
                ('eth', models.CharField(max_length=16)),
                ('dai', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Swaps_daily_stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swap_amount', models.CharField(max_length=8)),
                ('swap_currency', models.CharField(max_length=8)),
                ('tx_id', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commitment', models.CharField(max_length=128)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='explorer.block')),
            ],
        ),
        migrations.CreateModel(
            name='Kernel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.FloatField()),
                ('kernel_id', models.CharField(max_length=128)),
                ('minHeight', models.IntegerField()),
                ('maxHeight', models.CharField(max_length=128)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kernels', to='explorer.block')),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commitment', models.CharField(max_length=128)),
                ('height', models.IntegerField()),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='explorer.block')),
            ],
        ),
        migrations.CreateModel(
            name='Contract_funds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.IntegerField()),
                ('value', models.CharField(blank=True, max_length=32, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funds', to='explorer.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Contract_calls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('cname', models.CharField(blank=True, max_length=32, null=True)),
                ('imethod', models.IntegerField()),
                ('methodname', models.CharField(blank=True, max_length=32, null=True)),
                ('faction', models.CharField(blank=True, max_length=32, null=True)),
                ('fval', models.CharField(blank=True, max_length=32, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calls', to='explorer.contract')),
            ],
        ),
    ]
