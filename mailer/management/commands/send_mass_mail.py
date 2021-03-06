import logging

from django.conf import settings
from django.core.management.base import NoArgsCommand

from mailer.engine import send_mass


# allow a sysadmin to pause the sending of mail temporarily.
PAUSE_SEND = getattr(settings, "MAILER_PAUSE_SEND", False)


class Command(NoArgsCommand):
    help = "Do one pass through the mail queue, attempting to send mass mail according to settings."

    def handle_noargs(self, **options):
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        logging.info("-" * 72)
        # if PAUSE_SEND is turned on don't do anything.
        if not PAUSE_SEND:
            send_mass()
        else:
            logging.info("mass sending is paused, quitting.")
