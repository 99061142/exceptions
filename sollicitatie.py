# Array with all the questions that gets asked
questions = {
    "years": [
        "Hoeveel jaar praktijkervaring heeft u met dieren-dressuur",
        "Hoeveel jaar praktijkervaring heeft u met jongleren",
        "Hoeveel jaar praktijkervaring heeft u met acrobatiek",
        "Wat is uw lengte (in cm)"
    ],
    
    "strings": [ 
        "Bent u in het bezit van een Diploma MBO-4 ondernemen",
        "Bent u in het bezit van een geldig Vrachtwagen rijbewijs",
        "Bent u in het bezit van een hoge hoed",
        "Wat is uw lichaamsgewicht",
        "Heeft u het Certificaat 'Overleven met gevaarlijk personeel"
    ],

    "useless": [
        "Heeft u huisdieren",
        "Bent u in het bezit van een motor rijbewijs",
        "Heeft u een kind",
        "Wat is uw favoriete toetje"
    ]
}



# Array with the questions that gets asked with the users gender
questions_gender = {
    "male": [
        "Is uw snor breder dan 10 cm"
    ],

    "female": [
        "Draagt u rood krulhaar langer dan 20 cm"
    ]
}


answers = {
    "years": {
        "need": [4, 5, 3, 150],
        "answer": []
    },
    "strings": []
}


# Starting explanation how the program works
def start_explanation():
    print(
        "LET OP, als er wordt gevraagd of je een man bent, en je vult iets anders dan 'ja', wordt het als 'nee' opgevat",
        "LET OP, als je niks invult, of iets anders dan 'ja' antwoord, wordt het automatisch als 'nee' opgevat",
        "LET OP, als er gevraagd wordt hoeveel jaar u iets heeft, of wat uw lengte is, hoef je alleen een getal in te vullen. Anders wordt het als '0' opgevat",
        "",
        sep="\n", end="\n"
    )



def user_gender() -> str:
    genders = ("man", "vrouw")

    choosing_answer = True

    while choosing_answer:
        gender = input(f"Wat voor geslacht bent u? U kunt kiezen tussen  {' / '.join(genders)}: ").lower()
        
        if gender in genders:
            choosing_answer  = False

    return gender


"""
#questions['strings'] += questions_gender[gender] # Add the questions to the questions string array




# Ask the questions that need a year, and add them to the answers array
for question in questions['years']:
    question += "? "

    answer = input(question)

    answers['years']['answer'].append(answer)


# Ask the questions that only need a 'yes' or 'no', and add them to the answers array

for question in questions['strings']:
    question += "? "

    answer = input(question).lower()

    answers['strings'].append(answer)


# Ask the questions that don't matter

for question in questions['useless']:
    question += "? "

    input(question)


# Check if the questions are correctly answered

def application_validation():

    validation = True

    # Check all the questions (what the user can answer with a year) to see if is equal or higher than the years that are needed
    
    try:
        for num, value in enumerate( answers['years']['answer'] ):
                if int(value) < answers['years']['need'][num]:
                    validation = False
    
    except:
        validation = False


    # Check all the questions (what the user can answer with 'ja' or 'nee') to see if all the questions are answered with 'yes'
    
    for value in answers['strings']:
        if value != "ja":
            validation = False

    return validation # Return if the user has answered everything correctly
"""


def main():
    start_explanation()

    gender = user_gender()


    suited = application_validation()

    if suited:
        print("Uw applicatie is goedgekeurd.")
    else:
        print("Uw applicatie is niet goedgekeurd.")




# When the program starts
if __name__ == "__main__":
    main()    