from django.test import TestCase

# Create your tests here.


class Test(TestCase):
    '''This is the test for the app1'''

    def test_index_view(self):
        '''This is the test for the index view'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
