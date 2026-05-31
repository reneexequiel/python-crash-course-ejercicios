from survey import AnonymousSurvey

#define una pregunta y crea una encuenta
question = "que lenguaje aprendiste primero?"
my_survey = AnonymousSurvey(question)

#muestra las preguntas, y almacena las respuestas de las preguntas
my_survey.show_question()
print("Enter 'q' en cualquier momento para salir.\n")

while True:
    responses = input("Lenguaje")
    if responses == 'q':
        break
    my_survey.store_responses(responses)

#muestra el resultado de la encuesta
print("\nGracias a todos por participar en la encuesta.")
my_survey.show_results()