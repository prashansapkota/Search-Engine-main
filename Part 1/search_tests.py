from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)

    def test_search(self):
        # Testing basic search function with the keyword 'music' using the provided articles. 
        expected_music_results = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
        self.assertEqual(search('music'), expected_music_results)
        # Testing search with an empty string, which should return an empty list.
        self.assertEqual(search(''), [])
        # Testing case insensitivity by ensuring 'MUSIC' returns the same results as 'music'.
        self.assertEqual(search('MUSIC'), search('music'))

    def test_title_length(self):
        titles = ['Short', 'Medium length', 'This is a very long title']
        # Testing title_length function by setting a max length of 10. Only titles with 10 or fewer characters should be returned.
        self.assertEqual(title_length(10, titles), ['Short'])
        # Testing title_length function where the max length is greater than any title. All titles should be included.
        self.assertEqual(title_length(30, titles), titles)
        # Testing title_length function with an unreasonably low max length (1). No titles should be returned.
        self.assertEqual(title_length(1, titles), [])

    def test_article_count(self):
        titles = ['Article 1', 'Article 2', 'Article 3', 'Article 4']
        # Testing article_count function with a count of 2. The function should return the first 2 articles from the list.
        self.assertEqual(article_count(2, titles), ['Article 1', 'Article 2'])
        # Testing article_count function where the requested count is greater than the number of articles available. 
        self.assertEqual(article_count(5, titles), titles)
        # Testing article_count function with a count of 0. An empty list should be returned.
        self.assertEqual(article_count(0, titles), [])

    def test_random_article(self):
        titles = ['Article 1', 'Article 2', 'Article 3']
         # Testing random_article function with a valid index of 1. The second article from the list should be returned.
        self.assertEqual(random_article(1, titles), 'Article 2')
        # Testing random_article function with an index of 0. The first article should be returned.
        self.assertEqual(random_article(0, titles), 'Article 1')
        # Testing random_article function with an out-of-bounds index. An empty string should be returned.
        self.assertEqual(random_article(3, titles), '')

    def test_favorite_article(self):
        titles = ['Python', 'Java', 'C++']
        # Testing article present
        self.assertTrue(favorite_article('Python', titles))
        # Testing case insensitivity
        self.assertTrue(favorite_article('JAVA', titles))
        # Testing article not present
        self.assertFalse(favorite_article('Ruby', titles))

    def test_multiple_keywords(self):
        initial_titles = ['Python programming', 'Java basics']
        # Testing adding new articles
        self.assertEqual(multiple_keywords('music', initial_titles), 
                         ['Python programming', 'Java basics'] + search('music'))
        # Testing no new articles
        self.assertEqual(multiple_keywords('nonexistent', initial_titles), initial_titles)
        # Testing case insensitivity
        self.assertEqual(multiple_keywords('PYTHON', initial_titles), 
                         ['Python programming', 'Java basics', 'Python (programming language)'])

    

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()