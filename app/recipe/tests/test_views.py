from django.test import SimpleTestCase
from recipe.views import RecipeViewSet


class RecipeViewSetTest(SimpleTestCase):

    def setUp(self):
        self.rvs = RecipeViewSet()

    def test_params_to_ints(self):
        str_int_list = '1,2,3'
        int_list = self.rvs._params_to_ints(str_int_list)
        self.assertEqual(int_list, [1, 2, 3])
