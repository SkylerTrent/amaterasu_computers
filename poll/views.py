
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Voted


# Create your views here.
def view_poll(request):
    """
    Function to pass the products with their respective
    nr of votes. It will check the model Voted to see
    if the user has already voted. Setting the voted
    var accordingly.
    It will calculate the total nr of votes.
    It will pass the list of voteable products,
    total nr of votes and the voted variable.
    """
    if request.user.is_authenticated:
        all_emails = Voted.objects.values_list('user_email', flat=True)
        current_user_email = request.user.email
        if current_user_email in all_emails:
            voted = True
        else:
            voted = False
    else:
        voted = False

    total_votes = 0
    for product_type in Poll.objects.all():
        total_votes += product_type.votes

    poll_product_list = Poll.objects.order_by('id')
    template = 'poll/poll.html'
    context = {
        'poll_product_list': poll_product_list,
        'voted': voted,
        'total_votes': total_votes,
    }

    return render(request, template, context)


def add_vote(request, poll_product_id):
    """
    This functions adds a vote to the product that corresponds with the
    button pressed. Before adding the vote to the counter it checks
    the model 'voted' to see if the user's emailadres is present.
    If not, the emailadres is added to the field and the vote is
    incremented.
    """
    product_type = get_object_or_404(Poll, pk=poll_product_id)
    current_user_email = request.user.email
    all_emails = Voted.objects.values_list('user_email', flat=True)
    redirect_url = request.POST.get('redirect_url')
    if current_user_email not in all_emails:
        product_type.votes += 1
        product_type.save()
        Voted.objects.create(user_email=current_user_email)

    return redirect(redirect_url)