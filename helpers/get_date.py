import locale
import pytz
from datetime import datetime, timedelta


def current_date(lang, loc) -> str:
    locale.setlocale(locale.LC_ALL, f"{lang}_{loc}")
    date_format = "%A %-d. %b"
    date_now = datetime.now()
    date = date_now.strftime(date_format)
    return date


def past_date():
    date_format = "%-d. %B %Y"
    date_now = datetime.now(tz=pytz.timezone('CET'))
    current_date = date_now.strftime(date_format)
    past_date = (date_now - timedelta(days=15)).strftime(date_format)
    timestamp = (date_now - timedelta(days=15)).replace(hour=1, minute=0, second=0).strftime("%s")
    return {
        "current_date": current_date,
        "past_date": past_date,
        "timestamp": timestamp
    }


def get_month():
    locale.setlocale(locale.LC_ALL, "de_DE")
    date_format = "%B %Y"
    date_format_tariff = "%d/%m/%Y"
    current_month = datetime.now().replace(day=1, hour=1, minute=0, second=0)
    prev_month = (current_month - timedelta(days=1)).replace(day=1, hour=1, minute=0, second=0).strftime(date_format)
    prev_month_tariff = (current_month - timedelta(days=1)).replace(day=1, hour=1, minute=0, second=0).strftime(date_format_tariff)
    timestamp_current_month = current_month.strftime("%s")
    timestamp_prev_month = (current_month - timedelta(days=1)).replace(day=1, hour=1, minute=0, second=0).strftime("%s")
    return {
        "prev_month": prev_month,
        "prev_month_tariff": prev_month_tariff,
        "timestamp_current_month": timestamp_current_month,
        "timestamp_prev_month": timestamp_prev_month
    }
