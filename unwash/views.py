from django.views.generic import DetailView
from stores.views import StoreListView, Store


class SalonListView(StoreListView):
    template_name = 'unwash/salon.html'

    def get_title(self):
        return 'Select your favorite salon'


class SalonSelectView(DetailView):
    def get(self, request, *args, **kwargs):
        store = Store.objects.get(pk=kwargs['pk'])

        raise Exception(store)

        return super(SalonSelectView, self).get(request, *args, **kwargs)
