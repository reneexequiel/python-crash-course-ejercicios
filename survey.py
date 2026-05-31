

class AnonymousSurvey():
    """coleccionar una serie de respuestas para una encuesta"""
    def __init__(self, question):
        """almacenar una pregunta, y preparar para almacenar respuestas"""
        self.question = question
        self.responses = []

    def show_question(self):
        """mostrar las preguntas de encuestas"""
        print(self.question)

    def store_responses(self, new_response):
        """almacena una sola respuesta de la encuesta"""
        self.responses.append(new_response)

    def show_results(self):
        """muestra todas las respuestas que ban sido dadas"""
        print("Resultado Encuesta:")
        for response in self.responses:
            print('- ' + response)