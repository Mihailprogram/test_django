from django.shortcuts import redirect, render
from allauth.socialaccount.models import SocialAccount
from .models import Place
from .forms import PlaceForm

# Create your views here.


def profile(request):
    firs_name = SocialAccount.objects.filter(
        user=request.user, provider='vk')[0].extra_data['first_name']
    last_name = SocialAccount.objects.filter(
        user=request.user, provider='vk')[0].extra_data['last_name']
    photo = SocialAccount.objects.filter(
        user=request.user, provider='vk')[0].extra_data['photo_big']
    all_places = Place.objects.filter(user=request.user).order_by('-id')
    context = {
        'firs_name': firs_name,
        'last_name': last_name,
        'photo': photo,
        'all_places': all_places,

    }
    return render(request, 'user/profile.html', context)


def map_view(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('places:profile')
    else:
        form = PlaceForm()

    return render(request, 'user/map.html', {'form': form})
