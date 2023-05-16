import datetime

from django.core.management.base import BaseCommand

from place.models import Answer, Comment, Option, Place


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--start-date",
            "-s",
            help="Date to start answers",
        )
        parser.add_argument(
            "--number",
            "-n",
            help="Number of answers to create following start date",
        )
        parser.add_argument(
            "--place",
            "-p",
            help="Place to create answers for",
        )
        parser.add_argument(
            "--option",
            "-o",
            help="Option to create answers for",
        )

    def handle(self, *args, **options):
        start_date = (
            options["start_date"] if options["start_date"] else datetime.date.today()
        )
        number = int(options["number"]) if options["number"] else 1

        place = (
            Place.objects.get(uuid=options["place"])
            if options["place"]
            else Place.objects.first()
        )
        option = (
            Option.objects.get(uuid=options["option"])
            if options["option"]
            else Option.objects.first()
        )
        answer = Answer.objects.create(
            start_date=start_date,
            duration=number,
            place=place,
            option=option,
            created_by=place.created_by,
        )
        Comment.objects.create(
            text="Comment for answer",
            answer=answer,
            author=answer.created_by,
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Created answer, starting {answer.start_date} for {number} day(s) and for place {place.name}"
            )
        )
