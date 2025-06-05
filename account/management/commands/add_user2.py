import uuid
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from account.models import CustomUser, Role, RoleName
from faker import Faker
from django.contrib.auth.hashers import make_password

fake = Faker()

class Command(BaseCommand):
    help = "Generate 10,000 students with role STUDENT"

    def handle(self, *args, **kwargs):
        student_role, created = Role.objects.get_or_create(name=RoleName.STUDENT)

        created_count = 0

        users = [CustomUser(username=f"user1{_}", email=f"fakeemail{_}@example.com", first_name=f"fake first name {_}", last_name=f"fake lastname {_}", phone="+998990001219", role=student_role, custom_uuid=uuid.uuid4(), is_worker=False, is_verified=True, password=make_password(f"defaultpassword123{_}")) for _ in range(100, 1000)]
        print(users)
        print("list users")
        CustomUser.objects.bulk_create(users)
        created_count += len(users)

        self.stdout.write(self.style.SUCCESS(f"✅ Successfully created {created_count} STUDENT users"))
