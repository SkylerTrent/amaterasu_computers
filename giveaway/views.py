
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Giveaway, Has_Voted


# Create your views here.
def view_giveaway(request):
    if request.user.is_authenticated:
        all_emails = Has_Voted.objects.values_list('user_email', flat=True)
        current_user_email = request.user.email
        if current_user_email in all_emails:
            voted = True
        else:
            voted = False
    else:
        voted = False

    total_votes = 0
    for give_away_item in Giveaway.objects.all():
        total_votes += give_away_item.votes

    give_away_item_list = Giveaway.objects.order_by('id')
    template = 'giveaway/giveaway.html'
    context = {
        'give_away_item_list': give_away_item_list,
        'voted': voted,
        'total_votes': total_votes,
    }

    return render(request, template, context)


def add_vote(request, give_away_item_id):
    give_away_item = get_object_or_404(Giveaway, pk=give_away_item_id)
    current_user_email = request.user.email
    all_emails = Has_Voted.objects.values_list('user_email', flat=True)
    redirect_url = request.POST.get('redirect_url')
    if current_user_email not in all_emails:
        give_away_item.votes += 1
        give_away_item.save()
        Has_Voted.objects.create(user_email=current_user_email)

    return redirect(redirect_url)
