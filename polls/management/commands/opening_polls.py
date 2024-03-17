from django.core.management import BaseCommand

from polls.models import Poll


class Command(BaseCommand):
    help = "Opening all unopened polls"

    def handle(self, *args, **kwargs) -> None:
        unopened_polls = Poll.objects.filter(opened=False)
        if len(unopened_polls) == 0:
            print("Nothing to open")
            return

        for poll in unopened_polls:
            poll.opened = True
            poll.save()

        print(f"Number of poll opened: {len(unopened_polls)}")

