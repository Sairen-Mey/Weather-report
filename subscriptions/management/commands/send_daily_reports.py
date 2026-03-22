from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from subscriptions.models import Subscription
from weather.models import WeatherSnapshot
from django.utils import timezone

class Command(BaseCommand):
    help = "Send a email using Django email backend"

    def handle(self, *args, **options):
        active_subs = Subscription.objects.filter(is_active=True)

        for sub in active_subs:
            latest_weahtersnapshot = WeatherSnapshot.objects.filter(city=sub.city).order_by('-created_at').first()

            if not latest_weahtersnapshot:
                self.stdout.write(self.style.WARNING(f"No weather data for this city: {sub.city.name}"))
                continue

            subject = f"Weather report for {sub.city.name}\n"

            message =(
                f"City: {sub.city.name}\n"
                f"Temperature: {latest_weahtersnapshot.temperature} gradusiv\n"
                f"Humidity: {latest_weahtersnapshot.humidity}\n"
                f"Wind speed: {latest_weahtersnapshot.wind_speed}\n"
                f"Description: {latest_weahtersnapshot.description}\n"
            )

            send_mail(
                subject=subject,
                message=message,
                from_email= "ttwinkovitch4@gmail.com",#- create work email
                recipient_list = [sub.email],
            )

            sub.last_sent_at = timezone.now()
            sub.save(update_fields=["last_sent_at"])

            self.stdout.write(self.style.SUCCESS(F"Email sent to {sub.email}"))
