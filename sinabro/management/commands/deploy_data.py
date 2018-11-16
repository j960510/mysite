from django.core.management.base import BaseCommand


from sinabro.models import Consultant


class Command(BaseCommand):
    def set_consaltants(self, count):
        for i in range(count):
            Consultant.objects.create(
                name=f'박보영{i}',
                description='테스트 Description' * 5,
                education='테스트 학력\n' * 10,
                experience='테스트 경력\n' * 10,
            )

    def handle(self, *args, **options):
        self.set_consaltants(20)
