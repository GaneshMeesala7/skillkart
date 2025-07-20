# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile  # Import your model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q


def home(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/success.html')
    else:
        form = UserProfileForm()
    return render(request, 'users/home.html', {'form': form})

def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'users/profile_list.html', {'profiles': profiles})

@api_view(['GET', 'POST'])
def api_profile_list(request):
    if request.method == 'GET':
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def edit_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form})

def delete_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'users/delete_profile.html', {'profile': profile})

def profile_list(request):
    query = request.GET.get('q')
    if query:
        profiles = UserProfile.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query)
        )
    else:
        profiles = UserProfile.objects.all()
    return render(request, 'users/profile_list.html', {'profiles': profiles})

@api_view(['GET'])
def api_overview(request):
    return Response({
        'List': '/api/profiles/',
        'Detail View': '/api/profiles/<int:id>/',
        'Create': '/api/profiles/create/',
        'Update': '/api/profiles/update/<int:id>/',
        'Delete': '/api/profiles/delete/<int:id>/',
    })

@api_view(['GET'])
def profile_list_api(request):
    profiles = UserProfile.objects.all()
    serializer = UserProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profile_detail_api(request, id):
    profile = UserProfile.objects.get(id=id)
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['POST'])
def profile_create_api(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def profile_update_api(request, id):
    profile = UserProfile.objects.get(id=id)
    serializer = UserProfileSerializer(instance=profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def profile_delete_api(request, id):
    profile = UserProfile.objects.get(id=id)
    profile.delete()
    return Response({'message': 'Deleted successfully'})
