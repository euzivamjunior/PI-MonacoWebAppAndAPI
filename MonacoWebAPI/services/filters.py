from datetime import datetime, timedelta
from django.contrib.admin.filters import DateFieldListFilter


class MyDateTimeFilter(DateFieldListFilter):
    def __init__(self, *args, **kwargs):
        super(MyDateTimeFilter, self).__init__(*args, **kwargs)

        today = datetime.today()

        self.links += ((
            ('Próximos 7 dias', {
                self.lookup_kwarg_until: str(today + timedelta(days=7)),
            }),
            ('Próximos 30 dias', {
                self.lookup_kwarg_until: str(today + timedelta(days=30)),
            }),
            ('Próximo Trimestre', {
                self.lookup_kwarg_until: str(today + timedelta(days=90))
            }),
        ))
