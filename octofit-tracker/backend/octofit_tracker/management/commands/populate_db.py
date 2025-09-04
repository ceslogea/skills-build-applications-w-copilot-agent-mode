from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Apenas insere dados de teste, sem deletar dados existentes
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        Activity.objects.create(user=ironman, type='Run', duration=30)
        Activity.objects.create(user=batman, type='Swim', duration=45)

        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        Workout.objects.create(name='Power Lift', description='Strength training for super strength')

        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
