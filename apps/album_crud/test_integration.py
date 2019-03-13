from django.test import TestCase, Client
from .models import Album

class ViewsTest(TestCase):

    @classmethod
    def setUpClass(cls):
        Album.objects.create(title="A Test Album", artist="Test Band", year=2022)
    
    #must have a teardown class created along with a setup class even if just a 'pass'
    @classmethod
    def tearDownClass(cls):
        pass

    def test_view_create(self):
        c = Client()
        form_data = {
            "title": "Dancing Queen",
            "artist": "Abba",
            "year": 1986
        }

        r = c.post('/create', form_data)
        
        #did it get created in the function?
        a = Album.objects.last()
        self.assertEqual(a.title, form_data['title'])
        self.assertEqual(a.artist, form_data['artist'])
        self.assertEqual(a.year, form_data['year'])
        
        # did it redirect?
        self.assertEqual(r.status_code, 302)

    
        ## Adding to the AlbumTest class we were working in already
    def test_view_edit(self):
        ## For this one, we have given you a good jumping off point, but it's still
        ## up to you to create the url and the view function to make this test pass
        c = Client()
        post_data = {
            "title": "A Test Edit",
            "artist" : "Test Artist Edit",
            "year": 3099
        }
        # This should edit the single album that is created by our setUp method
        response = c.post('/album/1/edit', post_data)
        # Let's make sure the view function eventually redirects
       
        # Let's test to make sure the edit worked
        edited = Album.objects.get(id = 1)
        self.assertEqual(edited.title, post_data['title'])
        self.assertEqual(edited.artist, post_data['artist'])
        self.assertEqual(edited.year, post_data['year'])
        self.assertEqual(response.status_code, 302)

    def test_view_delete(self):
        # Test to make sure a view function can retrieve an album based on an id being sent in the url
        # Test to make sure that this specific album gets deleted
        num_deleted = Album.objects.get(id = 1).delete()[0]
        self.assertEqual(num_deleted, 1)
    
    def test_view_read(self):
        c = Client()
        response = c.get('/1/read')
        self.assertEqual(response.context[id], '1')
        # Test to make sure a view function can retrieve an album based on an id being sent in the url
        # Make sure this single record is getting passed via context
       
        