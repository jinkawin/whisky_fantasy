from django.test import TestCase

# Create your tests here.
class SearchViewTests(TestCase):
    def test_index_view_with_no_product(self):
        """
        If no categories exist, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('app:search_by_price'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['product'], [])
