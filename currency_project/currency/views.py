from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import CurrencyRate, RateRequestLog
from .services.utils import fetch_usd_to_rub


def get_current_usd(request):
    last_request = RateRequestLog.objects.last()
    if last_request:
        time_since_last = timezone.now() - last_request.timestamp
        if time_since_last < timedelta(seconds=10):
            return JsonResponse({
                'error': "Между запросами должно пройти 10 секунд"
            }, status=403)

    rate = fetch_usd_to_rub()

    if rate is not None:
        CurrencyRate.objects.create(rate=rate)
        RateRequestLog.objects.create()

        last_rates = CurrencyRate.objects.order_by('-timestamp')[:10]
        return JsonResponse({
            'current_rate': rate,
            'last_rates': list(last_rates.values('rate'))
        })
    else:
        return JsonResponse({'error': "Не удалось получить курс от внешнего API"}, status=500)
