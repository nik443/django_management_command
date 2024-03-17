from django.core.management import BaseCommand

from polls.models import Poll


class Command(BaseCommand):
    help = "rename the poll on id"

    def add_arguments(self, parser):
        # параметр nargs="+" нужен в случае, если для параметра передаем список значений, например список id
        parser.add_argument("--ids_poll", type=int, nargs="+")
        parser.add_argument("--name", type=str)

    def handle(self, *args, **options):
        option_ids = options["ids_poll"]
        option_name = options["name"]
        for poll_id in option_ids:
            try:
                poll = Poll.objects.get(id=poll_id)
                poll.name = option_name
                poll.save()
            except Poll.DoesNotExist as e:
                print(f"Poll with id {poll_id} don't exist")
