from django.conf import settings
import structlog


def get_xeeaisto_logger(name):
    """This will add a `xeeaisto` prefix to logger for easy configuration."""

    return structlog.get_logger(
        f"xeeaisto.{name}",
        project="xeeaisto",
        environment=settings.ENVIRONMENT,
        service="xeeaisto-backend",
        module=name,
    )
