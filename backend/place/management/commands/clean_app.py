from django.core.management.base import BaseCommand
from place.models import Answer, Comment, Option, Place


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # TODO improve to get all models of app
        places = Place.objects.all()
        answers = Answer.objects.all()
        comments = Comment.objects.all()
        options = Option.objects.all()
        self.stdout.write(
            self.style.SUCCESS(
                f"Objtecs to be deleted: {places.count()} places, {comments.count()} comments, {answers.count()} answers, {options.count()} options"
            )
        )
        places.delete()
        answers.delete()
        comments.delete()
        options.delete()
