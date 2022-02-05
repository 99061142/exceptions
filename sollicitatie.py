# All the questions
questions = {
    "important": {
        "Hoeveel jaar praktijkervaring heeft u met dieren-dressuur": 4,
        "Hoeveel jaar praktijkervaring heeft u met jongleren": 5,
        "Hoeveel jaar praktijkervaring heeft u met acrobatiek": 3,
        "Wat is uw lengte (in cm)": 150,
        "Bent u in het bezit van een Diploma MBO-4 ondernemen": "ja",
        "Bent u in het bezit van een geldig Vrachtwagen rijbewijs": "ja",
        "Bent u in het bezit van een hoge hoed": "ja",
        "Wat is uw lichaamsgewicht": "ja",
        "Heeft u het Certificaat 'Overleven met gevaarlijk personeel": "ja"
    },

    "useless": {
        "Heeft u huisdieren": "",
        "Bent u in het bezit van een motor rijbewijs": "",
        "Heeft u een kind": "",
        "Wat is uw favoriete toetje": ""
    }
}

# Questions for a specific gender
gender_questions = {
    "man": {
        "Is uw snor breder dan 10 cm": ""
    },

    "vrouw": {
        "Draagt u rood krulhaar langer dan 20 cm": ""
    }
}

user_failed = False # If the user failed the specific questions


# Starting explanation how the program works
def start_explanation():
    print(
        "LET OP, als er wordt gevraagd of je een man bent, en je vult iets anders dan 'ja', wordt het als 'nee' opgevat",
        "LET OP, als je niks invult, of iets anders dan 'ja' antwoord, wordt het automatisch als 'nee' opgevat",
        "LET OP, als er gevraagd wordt hoeveel jaar u iets heeft, of wat uw lengte is, hoef je alleen een getal in te vullen. Anders wordt het als '0' opgevat",
        "",
        sep="\n", end="\n"
    )


# Ask the gender of the user
def user_gender() -> str:
    choosing_answer = True # If the user did not choose a valid answer

    gender_options = " / ".join(gender_questions) # All the gender options

    while choosing_answer:
        gender = input(f"Wat voor geslacht bent u? U kunt kiezen tussen {gender_options}: ").lower()

        # If the users answer is a valid option
        if gender in gender_questions:
            choosing_answer  = False

    return gender


# Add the question(s) for the users gender
def add_gender_questions(gender:str):
    questions[gender] = gender_questions[gender]


# Add the answer of the user
def add_user_answer(question_answer, answer:str):
    question_answer = answer


# Ask all the questions
def ask_questions():
    global user_failed # If the user failed the specific questions

    # Loop through every key
    for key, key_questions in zip(questions, questions.values()):
        # loop through every question
        for question in key_questions:
            question_answer = questions[key][question] # Specific answer for the question
            choosing_answer = True # If the user did not choose a valid answer
            correct_answer = False # If the user correctly answered the question 

            # If the user did not choose a valid answer
            while choosing_answer:
                answer = input(f"{question}?: ").lower()

                # If the user gave an number as answer
                if answer.isdigit():
                    answer = int(answer) # Change the answer of the user to a number


                # If the question need a specific answer
                if question_answer:
                    # If the types of the specific answer and the answer of the user are the same
                    if type(question_answer) == type(answer):
                        # If the answer of the user is not the same as the answer the question need
                        if question_answer != answer:
                            user_failed = True # The user failed the application

                # If the type of the answer the question need and the answer the user gave are not the same
                if type(question_answer) != type(answer) or not answer: 
                    error_message = "Kies een even getal (boven de -1)" if isinstance(question_answer, int) else "Kies nee/ja" # Error message what the user did wrong
                else:
                    correct_answer = True # The user correctly answered the question

                # If the user correctly answered the question
                if correct_answer:
                    add_user_answer(question_answer, answer) # Add the answer to the questions dictionary
                    choosing_answer = False # Go to the next question
                else:
                    print(error_message) # Show what the user did wrong


# Show if the user is a good candidate
def show_result():
    message = "Uw applicatie is niet goedgekeurd." if user_failed else "Uw applicatie is goedgekeurd."
    print(message)


def main():
    start_explanation() # Rules / explanation of the application
    gender = user_gender() # Ask the gender of the user
    add_gender_questions(gender) # Add the gender questions
    ask_questions() # Ask all the questions
    show_result() # Show if the user is a good candidate




# When the program starts
if __name__ == "__main__":
    main()    