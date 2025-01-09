from django.conf import settings
from django.shortcuts import render
from django.urls import URLResolver, get_resolver


def index(request):
    resolver = get_resolver()
    apps = []
    for app in settings.INSTALLED_APPS:
        if app.startswith("apps."):
            try:
                app_name = app.split(".")[-1]
                if app_name == "home":
                    continue
                for pattern in resolver.url_patterns:
                    if isinstance(pattern, URLResolver):
                        for subpattern in pattern.url_patterns:
                            if subpattern.pattern._route == "":
                                apps.append({"name": app_name})

            except Exception:
                continue

    return render(request, "home/home.html", {"apps": apps})
