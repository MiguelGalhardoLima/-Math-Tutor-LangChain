import re # import the regular expressions module
import json # import the json module to Python
print("Bem-vindos! Sou um professor virtual, faça sua pergunta!\nExemplos: Quanto é 2+2?\nResolva 5x=10")

def valid_perguntas(perguntas): # create a function to validate the question
    padrao = r"[\d+\-x÷=*]" # the pattern checks for numbers and mathematical operators
    return bool(re.search(padrao, perguntas)) # returns True if valid, False if not

def professor_virtual(perguntas):
    if not valid_perguntas(perguntas): # checks if the question is valid
        return "Desculpe, essa pergunta não é de matemática." # if not valid, return a message
    #
    respostas = {
        "Quanto é 2+2?": "2+2 é igual a 4.",
        "Resolva 5x=10": "Dividindo ambos os lados por 5, temos x=2"
    }

    return respostas.get(perguntas, "Desculpe, não sei responder essa pergunta ainda.") # if the question is not predefined, return a default message

def processar_perguntas(json_string):
    try:
        dados = json.loads(json_string) # load the JSON string to a Python dictionary
        perguntas = dados["perguntas"] # get the question from the JSON data

        if valid_perguntas(perguntas): # if the question is valid
            resposta = professor_virtual(perguntas) # get the answer
            return json.dumps({"respostas": resposta}, indent=4, ensure_ascii=False) # return the response in JSON format
        
        else: 
            return json.dumps({"erro": "Pergunta inválida"}, indent=4, ensure_ascii=False) # if the question is invalid, return an error message

    except json.JSONDecodeError:
        return json.dumps({"erro": "Entrada inválida. Por Favor, envie um JSON válido."}, indent=4, ensure_ascii=False) # if there's an error decoding JSON, return an error message

# Testing
json_input = '{"perguntas": "Quanto é 2+2?"}'
print(processar_perguntas(json_input))  # Expecting a JSON response with the answer to the question

json_input = '{"perguntas": "Qual a capital do Brasil?"}'
print(processar_perguntas(json_input))  # Expecting a JSON error response since it's not a math question
