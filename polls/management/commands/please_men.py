from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Jast print 'please men'"

    def handle(self, *args, **kwargs):
        print("please men")
