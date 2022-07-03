from __future__ import absolute_import, unicode_literals
import random
from celery import task
from .models import BillingItem
@task(name="sum_two_numbers")
def add(x, y):
    return x + y


@task(name="multiply_two_numbers")
def mul(item_name,x, y):
    name = item_name
    number_1 = x
    number_2 = (y * random.randint(3, 100))
    total = number_1 *number_2
    new_object = BillingItem.objects.create(item_name=name,number_1=number_1,number_2=number_2,total=total)
    return total


@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)