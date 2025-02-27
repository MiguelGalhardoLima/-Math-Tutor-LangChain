# Mathematical Tutor System

The **Mathematical Tutor System** is a simple system that simulates a virtual math tutor. It receives mathematical questions, validates the input, and processes the question with a **Virtual Professor** to provide the correct answer.

## Requirements
- **Python 3.x**
- No external libraries are required.

## How to Use

1. Download or clone this repository to your local machine using:
    ```bash
    git clone https://github.com/YOUR_USERNAME/Mathematical-Tutor-System.git
    ```

2. Navigate to the folder where the script is located and run:
    ```bash
    python main.py
    ```

3. The system will prompt you with a welcome message and ask you to enter a valid mathematical expression (e.g., `Quanto é 2+2?`, `Resolva 5x=10`, etc.). Simply input your expression, and the system will return the appropriate response in JSON format.

4. If you provide a non-mathematical question (e.g., `What is the capital of Brazil?`), the system will inform you that the question is invalid.

### Example Usage

Valid Mathematical Question:
```plaintext
Question: Quanto é 2+2?
Response:
{
  "respostas": "2+2 é igual a 4."
}
Question: Qual a capital do Brasil?
Response:
{
  "erro": "Pergunta inválida"
}
```
### How It Works
The system consists of two main components:

Receiver: The system receives a JSON input with a question and checks if it matches a mathematical query using regular expressions. If the input is valid, it forwards the question to the Virtual Professor. If the question is invalid, it returns an error message.

Virtual Professor: The Virtual Professor evaluates the valid mathematical question and returns a pre-defined response. If the question is not in the predefined set, it will return a default message stating that it doesn’t know the answer. If the question is not a valid mathematical question, the system will inform the user of the error.

### Future Improvements
Integration with LangChain: The next step is to integrate LangChain to improve the communication between agents and enhance the system's structure.
### Contributing
Feel free to contribute to this project by opening issues and submitting pull requests. Any contribution is welcome!
