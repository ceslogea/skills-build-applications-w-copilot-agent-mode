from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@user.com', team=team)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@user.com')
        self.assertEqual(user.team, team)
