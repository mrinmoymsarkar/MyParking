"""
Views for the main app
"""
import sys

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView


from django_slack import slack_message

from .models import ParkingUser


class IndexPage(LoginRequiredMixin, TemplateView):
    """
    This is the index page for the App. Requires login
    """
    template_name = 'app/index.html'


@login_required
def blocking(request):
    """
    View for blocking page
    """
    assert isinstance(request, HttpRequest)
    state = ''

    if request.POST:
        license_plate = request.POST.get('license')
        state = license_plate

        try:
            this_parking_user = None
            blocked_parking_user = None

            for p_usr in ParkingUser.objects.all():
                last3 = str(p_usr.licenseplate)[-3:]
                if last3 == str(license_plate):
                    state = p_usr.user.username
                    blocked_parking_user = p_usr
            this_parking_user = ParkingUser.objects.get(user=request.user)
            return inform_blockee(this_parking_user, blocked_parking_user, request)
        except:
            err = sys.exc_info()[0]
            print("Unexpected error:", err)
            state = 'No User Associated with this license'

    return render(request,'app/blocking.html',{'state':state,'title':'Blocking',})


    # return render(
    #     request,
    #     'app/blocking.html',
    #     context_instance=RequestContext(request,
    #                                     {'state':state,
    #                                      'title':'Blocking',}))

@login_required
def blocked(request):
    """
    View for blocked page
    """
    assert isinstance(request, HttpRequest)
    state = ''

    if request.POST:
        license_plate = request.POST.get('license')
        state = license_plate

        try:
            this_parking_user = None
            blocking_parking_user = None

            for p_usr in ParkingUser.objects.all():
                last3 = str(p_usr.licenseplate)[-3:]
                if last3 == str(license_plate):
                    state = p_usr.user.username
                    blocking_parking_user = p_usr

            this_parking_user = ParkingUser.objects.get(user=request.user)
            return inform_blocker(this_parking_user, blocking_parking_user, request)
        except:
            err = sys.exc_info()[0]
            print("Unexpected error:", err)
            state = 'No User Associated with this license'
    return render(
        request,
        'app/blocked.html',
        context_instance=RequestContext(request,
                                        {'state':state,
                                         'title':'Blocking',}))

@login_required
def inform_blockee(this_parking_user, blocked_parking_user, request):
    """
    View to inform blockee
    """
    send_mail('You Have Been Parked In By ' + str(this_parking_user.user.username),
              'Contact them at ' + str(this_parking_user.phonenumber),
              'parking@playstudios.com',
              [str(blocked_parking_user.user.email)],
              fail_silently=False)
    slack_message('slack/block.slack',
                  {'blockee': str(this_parking_user.user.username),
                   'blocked': str(blocked_parking_user.user.username),})

    return render(
        request,
        'app/blockingreported.html',
        context_instance=RequestContext(request,
                                        {'phonenumber': str(blocked_parking_user.phonenumber),
                                         'username':str(blocked_parking_user.user.username),
                                         'email':str(blocked_parking_user.user.email),}))

@login_required
def inform_blocker(this_parking_user, blocking_parking_user, request):
    """
    View to inform the blocked
    """
    send_mail('You Are Parking In ' + str(this_parking_user.user.username),
              'Their Phone Number: ' + str(this_parking_user.phonenumber),
              'parking@playstudios.com',
              [str(blocking_parking_user.user.email)],
              fail_silently=False)
    slack_message('slack/block.slack',
                  {'blockee': str(this_parking_user.user.username),
                   'blocked': str(blocking_parking_user.user.username),})

    return render(
        request,
        'app/blockerreported.html',
        context_instance=RequestContext(request,
                                        {'phonenumber': str(blocking_parking_user.phonenumber),
                                         'username':str(blocking_parking_user.user.username),
                                         'email':str(blocking_parking_user.user.email),}))
