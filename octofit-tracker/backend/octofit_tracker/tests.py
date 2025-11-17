from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='marvel')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel', description='Marvel Team')
        self.assertEqual(team.name, 'marvel')
        self.assertEqual(team.description, 'Marvel Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='marvel')
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2025-11-17')
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.duration, 30)
        self.assertEqual(str(activity.date), '2025-11-17')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='marvel', description='Marvel Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team.name, 'marvel')
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        self.assertEqual(workout.name, 'Pushups')
        self.assertEqual(workout.description, 'Do 20 pushups')
        self.assertEqual(workout.suggested_for, 'marvel')
