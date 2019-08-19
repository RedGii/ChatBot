from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    "Pico",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="./dbBrain.sqlite3",
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        }
    ]
)

# Cambiare il path del training.txt con il percorso corretto
with open("C:/Users/Pico/Desktop/bot/training.txt") as f:
    conversation = f.readlines()
    bot.set_trainer(ListTrainer)
    bot.train(conversation)


while True:
    try:
        user_input = input("Tu: ")
        response = bot.get_response(user_input)
        print("Pico:", response)
    except(KeyboardInterrupt, SystemExit):
        print("A presto!")
        break
