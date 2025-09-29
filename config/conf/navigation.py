from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",   # uycha
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Accounts"),
        "separator": True,
        "items": [
            {
                "title": _("Umumiy foydalanuvchilar"),
                "icon": "group",  # odamlar
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
            {
                "title": _("Manajer"),
                "icon": "person",  # rejissyor (kino kamerasiga o‘xshash)
                "link": reverse_lazy("admin:accounts_managermodel_changelist"),
            },
            {
                "title": _("Actors"),
                "icon": "person",  # aktyor
                "link": reverse_lazy("admin:accounts_actorprofilemodel_changelist"),
            },
            {
                "title": _("Rejisyor"),
                "icon": "movie",  # rejissyor (kino kamerasiga o‘xshash)
                "link": reverse_lazy("admin:accounts_directormodel_changelist"),
            },
        ],
    },
    {
        "title": _("Anime Management"),
        "separator": True,
        "items": [
            {
                "title": _("Anime"),
                "icon": "animation",  # anime uchun
                "link": reverse_lazy("admin:api_animemodel_changelist"),
            },
            {
                "title": _("Calendar Events"),
                "icon": "event",  # taqvim belgisi
                "link": reverse_lazy("admin:api_calendareventmodel_changelist"),
            },
            {
                "title": _("Countries"),
                "icon": "public",  # globus
                "link": reverse_lazy("admin:api_countrymodel_changelist"),
            },
            {
                "title": _("Studios"),
                "icon": "business",  # bino/studiya
                "link": reverse_lazy("admin:api_studiomodel_changelist"),
            },
            {
                "title": _("Years"),
                "icon": "calendar_today",  # yil (kalendar)
                "link": reverse_lazy("admin:api_yearmodel_changelist"),
            },
        ],
    },
]
