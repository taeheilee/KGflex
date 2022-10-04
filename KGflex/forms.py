from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import KGflex, Notice, KDrama, UMovie, KMovie, entertainment
from django.utils.safestring import mark_safe

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

class KGflexCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})       
    class Meta:
          model = KGflex
          fields = ('title', 'file_upload', 'content')

class CustomFileWidget(forms.FileInput):
    def __init__(self, attrs={}):
      super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
         file_name = value.url.split('/')[-1]
         output.append(super().render(name, value, attrs))
         output.append(f'<span class="form-control">첨부파일 : <a class="text-reset text-decoration-none" target="_blank" href="{value.url}">{file_name}</a><input class="form-check-input ms-2 me-1" type="checkbox" name="upload_clear" id="upload_clear_id" value="upload_del">Delete</span>')
         return mark_safe(u''.join(output))
        output.append(super().render(name, value, attrs))
        return mark_safe(u''.join(output)) 

class KGflexUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})
  
    class Meta:
        model = KGflex
        fields = ('title', 'file_upload', 'content')
        widgets = {
        'file_upload': CustomFileWidget,
        }         

class NoticeCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})       
    class Meta:
          model = Notice
          fields = ('title', 'file_upload', 'content')



class NoticeCustomFileWidget(forms.FileInput):
    def __init__(self, attrs={}):
      super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
            file_name = value.url.split('/')[-1]
            output.append(super().render(name, value, attrs))
            output.append(f'<span class="form-control">첨부파일 : <a class="text-reset text-decoration-none" target="_blank" href="{value.url}">{file_name}</a><input class="form-check-input ms-2 me-1" type="checkbox" name="upload_clear" id="upload_clear_id" value="upload_del">Delete</span>')
            return mark_safe(u''.join(output))
        output.append(super().render(name, value, attrs))
        return mark_safe(u''.join(output))


class NoticeUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})
    class Meta:
        model = Notice
        fields = ('title', 'file_upload', 'content')
        widgets = {
         'file_upload': NoticeCustomFileWidget,
        }

class KDramaCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})       
    class Meta:
          model = KDrama
          fields = ('title', 'file_upload', 'content')



class KDramaCustomFileWidget(forms.FileInput):
    def __init__(self, attrs={}):
      super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
            file_name = value.url.split('/')[-1]
            output.append(super().render(name, value, attrs))
            output.append(f'<span class="form-control">첨부파일 : <a class="text-reset text-decoration-none" target="_blank" href="{value.url}">{file_name}</a><input class="form-check-input ms-2 me-1" type="checkbox" name="upload_clear" id="upload_clear_id" value="upload_del">Delete</span>')
            return mark_safe(u''.join(output))
        output.append(super().render(name, value, attrs))
        return mark_safe(u''.join(output))


class KDramaUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})
    class Meta:
        model = KDrama
        fields = ('title', 'file_upload', 'content')
        widgets = {
         'file_upload': KDramaCustomFileWidget,
        }





















class UMovieCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})       
    class Meta:
          model = UMovie
          fields = ('title', 'file_upload', 'content')



class UMovieCustomFileWidget(forms.FileInput):
    def __init__(self, attrs={}):
      super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
            file_name = value.url.split('/')[-1]
            output.append(super().render(name, value, attrs))
            output.append(f'<span class="form-control">첨부파일 : <a class="text-reset text-decoration-none" target="_blank" href="{value.url}">{file_name}</a><input class="form-check-input ms-2 me-1" type="checkbox" name="upload_clear" id="upload_clear_id" value="upload_del">Delete</span>')
            return mark_safe(u''.join(output))
        output.append(super().render(name, value, attrs))
        return mark_safe(u''.join(output))


class UMovieUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})
    class Meta:
        model = UMovie
        fields = ('title', 'file_upload', 'content')
        widgets = {
         'file_upload': UMovieCustomFileWidget,
        }




















class KMovieCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})       
    class Meta:
          model = KMovie
          fields = ('title', 'file_upload', 'content')



class KMovieCustomFileWidget(forms.FileInput):
    def __init__(self, attrs={}):
      super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
            file_name = value.url.split('/')[-1]
            output.append(super().render(name, value, attrs))
            output.append(f'<span class="form-control">첨부파일 : <a class="text-reset text-decoration-none" target="_blank" href="{value.url}">{file_name}</a><input class="form-check-input ms-2 me-1" type="checkbox" name="upload_clear" id="upload_clear_id" value="upload_del">Delete</span>')
            return mark_safe(u''.join(output))
        output.append(super().render(name, value, attrs))
        return mark_safe(u''.join(output))


class KMovieUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})
    class Meta:
        model = KMovie
        fields = ('title', 'file_upload', 'content')
        widgets = {
         'file_upload': KMovieCustomFileWidget,
        }





















class entertainmentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})       
    class Meta:
          model = entertainment
          fields = ('title', 'file_upload', 'content')



class entertainmentCustomFileWidget(forms.FileInput):
    def __init__(self, attrs={}):
      super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
            file_name = value.url.split('/')[-1]
            output.append(super().render(name, value, attrs))
            output.append(f'<span class="form-control">첨부파일 : <a class="text-reset text-decoration-none" target="_blank" href="{value.url}">{file_name}</a><input class="form-check-input ms-2 me-1" type="checkbox" name="upload_clear" id="upload_clear_id" value="upload_del">Delete</span>')
            return mark_safe(u''.join(output))
        output.append(super().render(name, value, attrs))
        return mark_safe(u''.join(output))


class entertainmentUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})
    class Meta:
        model = entertainment
        fields = ('title', 'file_upload', 'content')
        widgets = {
         'file_upload': entertainmentCustomFileWidget,
        }