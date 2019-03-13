# urls - do they call the proper function
# models - create, update, read, destroy properly?
# views - lots down here, talks to urls, talks to models, etc. So here we're testing did the full feature work? 

from django.test import TestCase, Client
from django.urls import resolve
from .models import *

class AlbumTest(TestCase):

    def test_index(self):

        self.assertEqual(resolve('/').view_name, 'apps.album_crud.views.index')
        self.assertEqual(resolve('/dash').view_name, 'apps.album_crud.views.dashboard')

        param = '42' #use this just to make it easier to see below that we're testing a param number and not using some magic number 42 for some specific reason.
        res = resolve(f'/album/{param}')
        #print(res.kwargs['album_id'])
        self.assertEqual(res.kwargs['album_id'], param)

#this is refactored url testing:
class AlbumTest(TestCase):

    #stores data in temp database to be used in tests so we don't have to create an album within every test where an album is referenced/tested
    @classmethod
    def setUpClass(cls):
        Album.objects.create(title="A Test Album", artist="Test Band", year=2022)
    
    #must have a teardown class created along with a setup class even if just a 'pass'
    @classmethod
    def tearDownClass(cls):
        pass

    def test_urls(self):
        c = Client()
        idx_response = c.get('/')
        self.assertEqual(idx_response.status_code, 200)
        create_response = c.get('/album/create')
        self.assertEqual(create_response.status_code, 302)

    def test_create_album(self):
        data = {
            "title": "Dark Side of the Moon",
            "artist": "Pink Floyd",
            "year": 1973
        }
        a = Album.objects.create(title = data['title'], artist = data['artist'], year = data['year'])
        self.assertEqual(a.title, data['title'])
        self.assertEqual(a.artist, data['artist'])
        self.assertEqual(a.year, data['year'])


    def test_get_album(self):
        a = Album.objects.first()
        self.assertEqual(a.id, 1)
        self.assertEqual(a.title, "A Test Album")

