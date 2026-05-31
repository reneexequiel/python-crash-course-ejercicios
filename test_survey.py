# # caso con una respuesta
# import unittest
# from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase): #el primer metodo que verificara que cuando
#     """test for the class AnonymousSurvey"""  #almacenamos una respuesta de la encuesta la respuesta termina en la lista de respuesta de la encuesta. 

#     def test_store_single_response(self):# si este test falla, sabremos que el metodo 
#                                         # sabremos desde el nombre del metodo mostrado en la salida del test fallido que fue un problema de almacenamiento de una sola respuesta de la encuesta 
#         """test that a single response is stored properly"""
#         question = "que lenguaje aprendiste primero?"
#         my_survey = AnonymousSurvey(question)#se crea una instancia con la pregunta, almacenamos una sola respuesta,
#         my_survey.store_responses('English')

#         self.assertIn('English', my_survey.responses)# se verifica que la respuesta fue almacenada correctamente.

# unittest.main()

#MISMO CASO PERO CON 3 RESPUESTAS

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """test for the class AnonymousSurvey"""

    def setUp(self):
        """se crea una encueta y se configura las respuestas para usarla en todos los metodos"""
        question = "que lenguaje aprendiste primero?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """test that a single response is stored properly"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """probar que 3 respuestas son almacenadas apropiadamente"""
        for response in self.responses:
            self.my_survey.store_responses(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()