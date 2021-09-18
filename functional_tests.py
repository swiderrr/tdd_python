from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edyta dowiedziała sie o nowej, wspaniałej aplikacji w postaci listy rzeczy do zrobienia
        # Postanowiła więc przejść na stronę główną tej aplikacji
        self.browser.get('http://localhost:8000')

        #Zwróciła uwagę, że tytuł strony i nagłówek zawierają słowo Listy.
        self.assertIn('Listy', self.browser.title)
        self.fail('Zakończenie testu')



if __name__ == '__main__':
    unittest.main(warnings='ignore')

#Od razu zostaje zachęcona, aby wpisać rzecz do zrobienia.

#W polu tekstowym wpisała "Kupić pawie pióra" (hobby Edyty
#polega na tworzeniu ozdobnych przynęt).

#Po naciśnięciu klawisza Enter strona została uaktulaniona i wyświetla
#"1: Kupić pawie pióra" jako element listy do zrobienia.

#Na stronie nadal znajduje się pole tekstowe zachęcające do podania kolejnego zadaniai.
#Edyta wpisała "Użyć pawich piór do zrobienia przynęty" (Edyta jest niezwykle skrupulatna).

# Strona została ponownie uaktulaniona i teraz wyświetla dwa elementy na liście rzeczy do zrobienia.

#Edyta była ciekawa, czy witryna zapamięta jej listę. Zwróciła uwagę na wygenerowany dla niej
#unikatowy adres URL,obok którego znajduje się pewien tekst z wyjaśnieniem

#Przechodzi pod podany adres URL i widzi wyświetloną swoją listę rzeczy do zrobienia.

#Usatysfakcjonowana kładzie się spać.

browser.quit()
