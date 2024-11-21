# Generated by Django 4.2.13 on 2024-08-23 14:38

from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps

from django_tasks import ResultStatus


def separate_results_field(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    DBTaskResult = apps.get_model("django_tasks_database", "DBTaskResult")

    DBTaskResult.objects.using(schema_editor.connection.alias).filter(
        status="COMPLETE"
    ).update(status=ResultStatus.SUCCEEDED)


def merge_results_field(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    DBTaskResult = apps.get_model("django_tasks_database", "DBTaskResult")

    DBTaskResult.objects.using(schema_editor.connection.alias).filter(
        status=ResultStatus.SUCCEEDED
    ).update(status="COMPLETE")


class Migration(migrations.Migration):
    dependencies = [
        ("django_tasks_database", "0010_alter_dbtaskresult_status"),
    ]

    operations = [migrations.RunPython(separate_results_field, merge_results_field)]
