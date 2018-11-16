from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo


class PhotoCreateView(CreateView):
    model = Photo
    fields = ['album', 'title', 'image', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PhotoCreateView, self).form_valid(form)


class PhotoChangeLV(ListView):
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)


class PhotoUpdateView(UpdateView) :
    model = Photo
    fields = ['album', 'title', 'image', 'description']

class PhotoDeleteView(DeleteView) :
    model = Photo

#--- Add/Change/Update/Delete for Album
#--- Change/Delete for Album
class AlbumChangeLV(ListView):
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

class AlbumDeleteView(DeleteView) :
    model = Album


#--- InlineFormSet View
#--- Add/Update for Album
from django.shortcuts import redirect
from photo.forms import PhotoInlineFormSet

class AlbumPhotoCV(CreateView):
    model = Album
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(AlbumPhotoCV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('photo:album_detail', pk=self.object.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AlbumPhotoUV(UpdateView):
    model = Album
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(AlbumPhotoUV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

