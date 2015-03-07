from pennyauction.libs.views import BaseView
from web.auctions.models import Item
from web.auctions.renderers import ItemRenderer


class DashboardView(BaseView):
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        items = [ItemRenderer(item) for item in Item.get_list_of_all_items()]

        return super(DashboardView, self).get_context_data(items=items, **kwargs)

    def get(self):
        return self.get_context_data()


def dashboard_view(request):
    return DashboardView(request).respond_with()