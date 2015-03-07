from django.contrib.auth import get_user_model
from django.core.management.base import NoArgsCommand
User = get_user_model()

class Command(NoArgsCommand):
    help = 'Insert Test Data'

    def _header(self, message, is_title=False):
        self.stdout.write('%s %s %s' % ((is_title and '#' or '>') * 20, message, (is_title and '#' or '<') * 20))

    def handle_noargs(self, **options):
        self._header(self.help)
        user = User.objects.create_superuser(email='verdan.mahmood@gmail.com', password='123456')