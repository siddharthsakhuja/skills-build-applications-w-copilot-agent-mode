from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc'),
        ]

        # Activities
        Activity.objects.create(user='ironman@marvel.com', activity_type='run', duration=30, date=date.today())
        Activity.objects.create(user='batman@dc.com', activity_type='cycle', duration=45, date=date.today())

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Upper body', difficulty='easy')
        Workout.objects.create(name='Squats', description='Lower body', difficulty='medium')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
