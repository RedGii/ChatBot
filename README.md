# ChatBot
Una semplice implementazione di un Chatbot, utilizzando il linguaggio di programmazione Python.
La base di conoscenza iniziale è basata su un dataset costituito da frasi in lingua Italiana.


# Esempio 
Una conversazione tipica potrebbe essere qualcosa del genere:


utente: Ciao! Come stai?

bot: bene, e tu?

utente: anche io sto bene.

bot: Ti piace la pizza?


# Come funziona

Ogni volta che un utente inserisce un'istruzione, la libreria salva il testo che ha inserito e il testo a cui l'istruzione era in risposta. Poiché si ricevono più input, aumenta il numero di risposte a cui può rispondere e l'accuratezza di ciascuna risposta in relazione all'istruzione di input. Il programma seleziona la risposta di corrispondenza più vicina cercando l'istruzione nota di corrispondenza più vicina che corrisponde all'input, quindi restituisce la risposta più probabile a tale istruzione in base alla frequenza con cui ogni risposta viene emessa dalle persone con cui comunica il bot.
