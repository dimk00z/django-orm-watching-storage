from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, now


def get_duration(duration):
    td_in_seconds = duration.total_seconds()
    hours, remainder = divmod(td_in_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    hours = int(hours)
    is_strange = False
    if hours > 1:
        is_strange = True
    minutes = int(minutes)
    seconds = int(seconds)
    if minutes < 10:
        minutes = "0{}".format(minutes)
    if seconds < 10:
        seconds = "0{}".format(seconds)
    return "{}:{}:{}".format(hours, minutes, seconds), is_strange


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        duration, is_strange = get_duration(now() - visit.entered_at)
        non_closed_visits.append({
            "who_entered": visit.passcard.owner_name,
            "entered_at": localtime(visit.entered_at),
            "duration": duration,
            "is_strange": is_strange
        })
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
