from uuid import uuid4
from django.db import models
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    historico = HistoricalRecords(inherit=True)

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_index=True,
    )

    class Meta:
        abstract = True
