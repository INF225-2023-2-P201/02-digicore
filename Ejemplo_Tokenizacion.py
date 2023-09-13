import nltk
import random
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# Descarga recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
print("----------------------------------")


frases = ["Quiero que Juan no tenga acceso a internet", 
            "Quiero que Alex no pueda salir a internet",
            "Ahora quiero que Juan si tenga acceso a internet",
            "Adam tendrá acceso a internet solo los lunes",
            "Quiero que Fran no pueda conectarse a internet"]

for i in frases:
    print("Frase: " + i)
    palabras = word_tokenize(i)

    partes_palabras = nltk.pos_tag(palabras)

    for j in partes_palabras:
        print(j)
        # print("Palabra: " + j[0] + ", Token: " + j[1])
    print("----------------------------------")

'''
Sustantivos (Nouns):
    NN: Sustantivo singular o incontable.
    NNS: Sustantivo plural.

Pronombres (Pronouns):
    PRP: Pronombre personal.
    PRP$: Pronombre posesivo.

Verbos (Verbs):
    VB: Verbo base (infinitivo).
    VBD: Verbo en pasado simple.
    VBG: Verbo en gerundio (presente continuo).
    VBN: Verbo en participio pasado.
    VBP: Verbo en presente simple.
    VBZ: Verbo en tercera persona del singular en presente simple.

Adjetivos (Adjectives):
    JJ: Adjetivo.
    JJR: Adjetivo comparativo.
    JJS: Adjetivo superlativo.

Adverbios (Adverbs):
    RB: Adverbio.
    RBR: Adverbio comparativo.
    RBS: Adverbio superlativo.

Preposiciones (Prepositions):
    IN: Preposición o subordinante.

Conjunciones (Conjunctions):
    CC: Conjunción coordinante.

Determinantes (Determiners):
    DT: Determinante.

Interjecciones (Interjections):
    UH: Interjección.

Puntuación (Punctuation):
    .: Punto.
    ,: Coma.
    : Punto y coma.
    (: Paréntesis de apertura.
    ): Paréntesis de cierre.
    "": Comillas.

Símbolos (Symbols):
    $: Símbolo de dólar.
    #: Símbolo de número.
    @: Símbolo de arroba.

'''