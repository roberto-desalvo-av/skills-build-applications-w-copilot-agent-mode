from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create users (super heroes)
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='marvel'),
            User(name='Iron Man', email='ironman@marvel.com', team='marvel'),
            User(name='Captain America', email='cap@marvel.com', team='marvel'),
            User(name='Batman', email='batman@dc.com', team='dc'),
            User(name='Superman', email='superman@dc.com', team='dc'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='dc'),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date='2025-11-17')
        Activity.objects.create(user=users[1], type='cycle', duration=45, date='2025-11-16')
        Activity.objects.create(user=users[3], type='swim', duration=60, date='2025-11-15')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Sprints', description='Run 5 sprints', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
