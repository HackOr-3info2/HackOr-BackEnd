# Generated by Django 4.2.7 on 2023-11-25 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("telefone", models.CharField(blank=True, max_length=20)),
                ("curriculo_lattes", models.CharField(blank=True, max_length=255)),
                ("formacao", models.CharField(blank=True, max_length=255)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "campus",
                    models.CharField(
                        choices=[
                            ("AL", "Abelardo Luz "),
                            ("AR", "Araquari"),
                            ("BL", "Blumenau"),
                            ("BR", "Brusque"),
                            ("CA", "Camboriú"),
                            ("CO", "Concórdia"),
                            ("FR", "Fraiburgo "),
                            ("IB", "Ibirama"),
                            ("LU", "Luzerna"),
                            ("RS", "Rio do Sul "),
                            ("CA", "Camboriú"),
                            ("SR", "Santa Rosa do Sul"),
                            ("SB", "São Bento do Sul"),
                            ("SF", "São Francisco do Sul"),
                            ("SO", "Sombrio "),
                            ("VI", "Videira"),
                        ],
                        default="AL",
                        max_length=2,
                    ),
                ),
                (
                    "capa",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="uploader.image",
                    ),
                ),
                (
                    "foto",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="uploader.image",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Comentario",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("description", models.CharField(max_length=255)),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tema",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "value",
                    models.CharField(choices=[("Like", "Like"), ("Unlike", "Unlike")], default="Like", max_length=10),
                ),
                ("comentario", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.comentario")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Hackathon",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ano", models.DateField(null=True)),
                (
                    "campus",
                    models.IntegerField(
                        choices=[
                            (1, "Abelardo Luz"),
                            (2, "Araquari"),
                            (3, "Blumenau"),
                            (4, "Brusque"),
                            (5, "Camboriú"),
                            (6, "Concórdia"),
                            (7, "Fraiburgo "),
                            (8, "Ibirama"),
                            (9, "Luzerna"),
                            (10, "Rio do Sul"),
                            (11, "Santa Rosa do Sul"),
                            (12, "São Bento do Sul"),
                            (13, "São Francisco do Sul"),
                            (14, "Sombrio "),
                            (15, "Videira"),
                        ]
                    ),
                ),
                ("turma", models.CharField(max_length=100)),
                ("estado", models.IntegerField(choices=[(1, "Pendente"), (2, "Em Andamento"), (3, "Concluído")])),
                ("data_inicio", models.DateTimeField(null=True)),
                ("data_final", models.DateTimeField(null=True)),
                ("fotos", models.ManyToManyField(related_name="+", to="uploader.image")),
                ("tema", models.ManyToManyField(related_name="hackathons", to="core.tema")),
            ],
        ),
        migrations.CreateModel(
            name="Equipe",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("tech", models.CharField(max_length=500)),
                (
                    "hackathon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="equipes", to="core.hackathon"
                    ),
                ),
                ("members", models.ManyToManyField(related_name="equipes", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name="comentario",
            name="hackathon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="comentarios", to="core.hackathon"
            ),
        ),
        migrations.AddField(
            model_name="comentario",
            name="liked",
            field=models.ManyToManyField(blank=True, related_name="liked", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="comentario",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="comentarios", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Avaliador",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                (
                    "hackathon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="avaliadores", to="core.hackathon"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="avaliadores",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Avaliacao",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "nota",
                    models.CharField(
                        choices=[("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
                        default="0",
                        max_length=1,
                    ),
                ),
                ("avaliador", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="core.avaliador")),
                ("categoria", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="core.categoria")),
                ("equipe", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="core.equipe")),
            ],
        ),
    ]
