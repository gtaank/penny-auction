from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = 'Insert Test Data'

    def _header(self, message, is_title=False):
        self.stdout.write('%s %s %s' % ((is_title and '#' or '>') * 20, message, (is_title and '#' or '<') * 20))

    def handle_noargs(self, **options):
        self._header(self.help)