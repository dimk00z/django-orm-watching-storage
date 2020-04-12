from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, now
from datacenter.storage_information_view import get_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    # Программируем здесь
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard=passcard):
        if visit.leaved_at:
            duration, is_strange = get_duration(
                visit.leaved_at-visit.entered_at)
        else:
            duration, is_strange = get_duration(
                now() - visit.entered_at)
        this_passcard_visits.append(
            {
                "entered_at": localtime(visit.entered_at),
                "duration": duration,
                "is_strange": is_strange
            })
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
