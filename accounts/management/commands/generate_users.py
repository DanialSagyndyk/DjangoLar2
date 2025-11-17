#Django Models
from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from django.contrib.auth.hashers import make_password
from faker import Faker
import random
from datetime import datetime, timedelta

#Django create command to generate users
class Command(BaseCommand):
    help = 'Generate 10,000 users'

    def handle(self, *args, **kwargs):
        fake = Faker()

        departments = ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
        roles = ['admin', 'manager', 'employee']

        users = []
        batch_size = 1000

        for i in range(10000):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.unique.email()

            user = CustomUser(
                email=email,
                username=fake.user_name(),
                first_name=first_name,
                last_name=last_name,
                phone=fake.phone_number(),
                city=fake.city(),
                country=fake.country(),
                department=random.choice(departments),
                role=random.choice(roles),
                bitrh_date=fake.date_of_birth(minimum_age=18, maximum_age=65),
                salary=random.randint(300000, 1200000),
                password=make_password('123456'),
            )
            users_batch.append(user)

            if len(users_batch) >= batch_size:
                CustomUser.objects.bulk_create(users_batch)
                users_batch = []
                self.stdout.write(f'Created {i + 1} users')

        if users_batch:
            CustomUser.objects.bulk_create(users_batch)

        self.stdout.write(self.style.SUCCESS('Successfully created 10,000 users'))

    


