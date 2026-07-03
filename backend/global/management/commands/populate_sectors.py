from django.core.management.base import BaseCommand
from designs.models import Design, Sector

sectors = [
    "Foreign Employment"
    "Tourism",
    "Travel",
    "Marketing"
]

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # 1. Create sectors if needed
        for name in sectors:
            Sector.objects.get_or_create(name=name)
        
        self.stdout.write(self.style.SUCCESS('Sectors populated successfully!'))