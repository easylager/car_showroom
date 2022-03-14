from celery import shared_task
from celery.utils.log import get_task_logger
from showroom.models import Showroom
from supplier.models import Supplier

logger = get_task_logger(__name__)


def get_features():
    showrooms = Showroom.objects.all()
    suppliers = Supplier.objects.all()

@shared_task
def search_car():
    showrooms = Showroom.objects.all()
