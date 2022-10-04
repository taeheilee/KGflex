from django.shortcuts import get_object_or_404, render, redirect
from KGflex.models import KGflex, Notice, KDrama, UMovie, KMovie, entertainment
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from KGflex.forms import UserForm, KGflexCreateForm, KGflexUpdateForm, NoticeCreateForm, NoticeUpdateForm, KDramaCreateForm, KDramaUpdateForm, UMovieCreateForm, UMovieUpdateForm, KMovieCreateForm, KMovieUpdateForm, entertainmentCreateForm, entertainmentUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from config import settings
import os
from django.core.exceptions import PermissionDenied

# Create your views here.

def KGflex_list(request):
    return render(request, 'KGflex/index.html')

class KGflexDetail(DetailView):
    model = KGflex
    template_name = 'KGflex/KGflex_detail.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
          return super().dispatch(request, *args, **kwargs)
        else:
          raise PermissionDenied

class KGflexList(ListView):
    model = KGflex
    template_name = 'KGflex/anime-details.html'
    ordering = '-pk'
    paginate_by = 10

class KGflexCreate(CreateView):
    model = KGflex
    form_class = KGflexCreateForm
    template_name = 'KGflex/KGflex_form.html'
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super().form_valid(form)
        else:
            return redirect('/KGflex')

@login_required(login_url='KGflex:login')
def KGflexDelete(request, pk):
    kgflex = get_object_or_404(KGflex, pk=pk)
    if request.user != kgflex.author:
        return redirect('KGflex:detail', pk=pk)
    if kgflex.file_upload:
        file_upload_path = os.path.join(settings.MEDIA_ROOT, kgflex.file_upload.path)
        if os.path.exists(file_upload_path):
            os.remove(file_upload_path)
    kgflex.delete()
    return redirect('KGflex:anime-details')

class KGflexUpdate(UpdateView):
    model = KGflex
    form_class = KGflexUpdateForm
    template_name = 'KGflex/KGflex_form_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
      if self.get_object().file_upload.name != '':
        if self.object.file_upload != self.get_object().file_upload.name:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
        if 'upload_clear' in self.request.POST:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
              self.object.file_upload = ''
      return super().form_valid(form)



class NoticeDetail(DetailView):
    model = Notice
    template_name = 'KGflex/notice_detail.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
          return super().dispatch(request, *args, **kwargs)
        else:
          raise PermissionDenied
          
class notice_list(ListView):
    model = Notice
    template_name = 'KGflex/notice.html'
    ordering = '-pk'
    paginate_by = 10

class NoticeCreate(CreateView):
    model = Notice
    form_class = NoticeCreateForm
    template_name = 'KGflex/notice_form.html'
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super().form_valid(form)
        else:
            return redirect('/KGflex')

@login_required(login_url='KGflex:login')
def NoticeDelete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.user != notice.author:
        return redirect('KGflex:notice_detail', pk=pk)
    if notice.file_upload:
        file_upload_path = os.path.join(settings.MEDIA_ROOT, notice.file_upload.path)
        if os.path.exists(file_upload_path):
            os.remove(file_upload_path)
    notice.delete()
    return redirect('KGflex:notice')

class NoticeUpdate(UpdateView):
    model = Notice
    form_class = NoticeUpdateForm
    template_name = 'KGflex/notice_form_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
            

    def form_valid(self, form):
      if self.get_object().file_upload.name != '':
        if self.object.file_upload != self.get_object().file_upload.name:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
        if 'upload_clear' in self.request.POST:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
              self.object.file_upload = ''
      return super().form_valid(form)

















class KDramaDetail(DetailView):
    model = KDrama
    template_name = 'KGflex/KDrama_detail.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
          return super().dispatch(request, *args, **kwargs)
        else:
          return redirect('/KGflex/login')
          
class KDrama_list(ListView):
    model = KDrama
    template_name = 'KGflex/KDrama.html'
    ordering = '-pk'
    paginate_by = 6

class KDramaCreate(CreateView):
    model = KDrama
    form_class =KDramaCreateForm
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super().form_valid(form)
        else:
            return redirect('/KGflex')

@login_required(login_url='KGflex:login')
def KDramaDelete(request, pk):
    kdrama = get_object_or_404(KDrama, pk=pk)
    if request.user != kdrama.author:
        return redirect('KGflex:KDrama_detail', pk=pk)
    if kdrama.file_upload:
        file_upload_path = os.path.join(settings.MEDIA_ROOT, kdrama.file_upload.path)
        if os.path.exists(file_upload_path):
            os.remove(file_upload_path)
    kdrama.delete()
    return redirect('KGflex:KDrama')





class KDramaUpdate(UpdateView):
    model = KDrama
    form_class = KDramaUpdateForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
      if self.get_object().file_upload.name != '':
        if self.object.file_upload != self.get_object().file_upload.name:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
        if 'upload_clear' in self.request.POST:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
              self.object.file_upload = ''
      return super().form_valid(form)
















class UMovieDetail(DetailView):
    model = UMovie
    template_name = 'KGflex/UMovie_detail.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
          return super().dispatch(request, *args, **kwargs)
        else:
          return redirect('/KGflex/login')
          
class UMovie_list(ListView):
    model = UMovie
    template_name = 'KGflex/UMovie.html'
    ordering = '-pk'
    paginate_by = 6

class UMovieCreate(CreateView):
    model = UMovie
    form_class =UMovieCreateForm
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super().form_valid(form)
        else:
            return redirect('/KGflex')

@login_required(login_url='KGflex:login')
def UMovieDelete(request, pk):
    umovie = get_object_or_404(UMovie, pk=pk)
    if request.user != umovie.author:
        return redirect('KGflex:UMovie_detail', pk=pk)
    if umovie.file_upload:
        file_upload_path = os.path.join(settings.MEDIA_ROOT, umovie.file_upload.path)
        if os.path.exists(file_upload_path):
            os.remove(file_upload_path)
    umovie.delete()
    return redirect('KGflex:UMovie')





class UMovieUpdate(UpdateView):
    model = UMovie
    form_class = UMovieUpdateForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
      if self.get_object().file_upload.name != '':
        if self.object.file_upload != self.get_object().file_upload.name:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
        if 'upload_clear' in self.request.POST:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
              self.object.file_upload = ''
      return super().form_valid(form)




















class entertainmentDetail(DetailView):
    model = entertainment
    template_name = 'KGflex/entertainment_detail.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
          return super().dispatch(request, *args, **kwargs)
        else:
          return redirect('/KGflex/login')
          
class entertainment_list(ListView):
    model = entertainment
    template_name = 'KGflex/entertainment.html'
    ordering = '-pk'
    paginate_by = 6

class entertainmentCreate(CreateView):
    model = entertainment
    form_class =entertainmentCreateForm
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super().form_valid(form)
        else:
            return redirect('/KGflex')

@login_required(login_url='KGflex:login')
def entertainmentDelete(request, pk):
    entert = get_object_or_404(entertainment, pk=pk)
    if request.user != entert.author:
        return redirect('KGflex:entertainment_detail', pk=pk)
    if entert.file_upload:
        file_upload_path = os.path.join(settings.MEDIA_ROOT, entert.file_upload.path)
        if os.path.exists(file_upload_path):
            os.remove(file_upload_path)
    entert.delete()
    return redirect('KGflex:entertainment')





class entertainmentUpdate(UpdateView):
    model = entertainment
    form_class = entertainmentUpdateForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
      if self.get_object().file_upload.name != '':
        if self.object.file_upload != self.get_object().file_upload.name:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
        if 'upload_clear' in self.request.POST:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
              self.object.file_upload = ''
      return super().form_valid(form)
















class KMovieDetail(DetailView):
    model = KMovie
    template_name = 'KGflex/KMovie_detail.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
          return super().dispatch(request, *args, **kwargs)
        else:
          return redirect('/KGflex/login')
          
class KMovie_list(ListView):
    model = KMovie
    template_name = 'KGflex/KMovie.html'
    ordering = '-pk'
    paginate_by = 6

class KMovieCreate(CreateView):
    model = KMovie
    form_class =KMovieCreateForm
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super().form_valid(form)
        else:
            return redirect('/KGflex')

@login_required(login_url='KGflex:login')
def KMovieDelete(request, pk):
    kmovie = get_object_or_404(KMovie, pk=pk)
    if request.user != kmovie.author:
        return redirect('KGflex:KMovie_detail', pk=pk)
    if kmovie.file_upload:
        file_upload_path = os.path.join(settings.MEDIA_ROOT, kmovie.file_upload.path)
        if os.path.exists(file_upload_path):
            os.remove(file_upload_path)
    kmovie.delete()
    return redirect('KGflex:KMovie')





class KMovieUpdate(UpdateView):
    model = KMovie
    form_class = KMovieUpdateForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
      if self.get_object().file_upload.name != '':
        if self.object.file_upload != self.get_object().file_upload.name:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
        if 'upload_clear' in self.request.POST:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
              self.object.file_upload = ''
      return super().form_valid(form)






















































def index(request):
    return render(request, 'KGflex/index.html')




    

def signup(request):
      if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=raw_password)
         login(request, user)
         return redirect('/')
      else:
         form = UserForm()
      return render(request, 'KGflex/signup.html', {'form': form})