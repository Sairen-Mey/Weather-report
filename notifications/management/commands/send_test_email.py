from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = "Send a test email using Django email backend"

    def add_arguments(self, parser):
        parser.add_argument("--to", required=True, help="Recipient email address")

    def handle(self, *args, **options):
        recipient = options["to"]

        subject = "Weather report: test email"
        message = "Hi, tratata"

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=False,
        )

        self.stdout.write(self.style.SUCCESS(f"sent test email to {recipient}"))