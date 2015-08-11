from django.shortcuts import render

from forms import MemberForm
from models import Member

def register(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = MemberForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            human = True
            # Save the new category to the database.
            new_member = form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return show_msg(request, str(new_member.id))
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = MemberForm()

    return render(request, 'add.html', {
        'page_title': 'Contact us',
        'form': form,
    })
    
def show_msg(request, mid):
    member = get_object_or_404(Message, id=mid)
    return render(request, 'show.html', {
        'page_title': 'member - '+ mid,
        'member': member,
    })
