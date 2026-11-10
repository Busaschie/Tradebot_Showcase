"""Auszug aus accounts/demo.py – Demo-Zugang mit festem Link.

Pro Besuch ein temporäres Konto ohne Passwort. Plätze zählen nach Aktivität (nicht nach Dauer),
abgelaufene Konten werden samt Läufen gelöscht (CASCADE)."""
from datetime import timedelta

from django.utils import timezone

ACCOUNT_HOURS = 48     # Lebensdauer eines Demo-Kontos
MAX_ACCOUNTS = 5       # gleichzeitig aktive Konten
IDLE_MINUTES = 60      # ohne Aktivität gibt ein Konto seinen Platz frei
MAX_TOTAL = 20         # vorhandene Konten insgesamt


def has_room() -> bool:
    return active_count() < MAX_ACCOUNTS and total_count() < MAX_TOTAL


def active_count() -> int:
    since = timezone.now() - timedelta(minutes=IDLE_MINUTES)
    return _alive().filter(last_login__gte=since).count()


def cleanup() -> int:
    old = _demo_users().filter(date_joined__lt=timezone.now() - timedelta(hours=ACCOUNT_HOURS))
    n = old.count()
    for user in old:
        user.delete()
    return n
