#from django.template import loader
#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, Http404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album


class IndexView (generic.ListView):
    template_name = 'Songs/index.html'
    context_object_name = 'all_albums'
    
    def get_queryset(self):
        return Album.objects.all()
    
    
class DetailView(generic.DetailView):
    model = Album
    template_name = 'Songs/details.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    
    
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    
class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('songs:index')
    
    
'''

Non Generic Views, we can also make generic views as above
----------------------------------------------------------



def index(request):
    all_albums = Album.objects.all()
    return render(request, 'Songs/index.html', {'all_albums' : all_albums})


'''






























'''
# Create your views here.



def index(request):
    #return HttpResponse("<h1>Sahil Kalra</h1>")
    all_albums = Album.objects.all()
    #template = loader.get_template('Songs/index.html')
    context = {
        'all_albums' : all_albums,
    }
    #html = ''
    #for album in all_album:
    #    url = '/songs/'+str(album.id)+'/'
    #    html += '<a href ="'+url+'">'+album.album_title+'</a><br>'
    #return HttpResponse(html)
    #return HttpResponse(template.render(context, request))
    return render(request, 'Songs/index.html', context)



def details(request, album_id):
    
    #try:
    #    album = Album.objects.get(id = album_id) -------|
    #except:                                             |
    #    raise Http404("Album not available")            |
    #                                                    |
    #                                                    |
    #                Can be replaced by<-----------------|
    
    album = get_object_or_404(Album,pk=album_id)
    
    context = {
        'album' : album,
    }
    #return HttpResponse("<h2>Detail for Album ID :" + str(album_id) +"</h2>")

    return render(request, 'Songs/details.html', context )


#def favorite(request, album_id):
    
 #   album = get_object_or_404(Album,pk=album_id)
 #   
 #   try:
 #       selected_song = album.song_set.get(pk=request.POST['song'])
 #   except:
 #       return render(request, 'Songs/details.html', {
 #           'album' : album,
 #           'error_message' : "Invalid selection"
 #       })
 #   else:
 #       selected_song.is_favorite = True
 #       selected_song.save()
 #       return render(request, 'Songs/details.html', {'album' : album})
        
'''