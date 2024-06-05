import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


class SQLSyntaxer:
    def __init__(self):
        self.model = load_model('syntaxer.keras')

        sql_syntax = pd.read_csv('queries_db_all.csv')

        self.tokenizer_nl = Tokenizer(filters='')
        self.tokenizer_nl.fit_on_texts(sql_syntax['nl'])

        self.tokenizer_sql = Tokenizer(filters='')
        self.tokenizer_sql.fit_on_texts(sql_syntax['syntax'])

        nl_sequences = self.tokenizer_nl.texts_to_sequences(sql_syntax['nl'])
        self.max_nl_length = max(len(seq) for seq in nl_sequences)

    def __decode_sequence(self, input_seq):
        decoded_sentence = ''
        for idx in input_seq:
            if idx == 0:
                continue
            word = self.tokenizer_sql.index_word.get(idx, '')
            decoded_sentence += word + ' '
        return decoded_sentence.strip()

    def translate(self, test_sentence):
        test_sequence = self.tokenizer_nl.texts_to_sequences([test_sentence])
        test_padded = pad_sequences(test_sequence, maxlen=self.max_nl_length, padding='post')
        predicted_sequence = self.model.predict(test_padded)
        predicted_sentence = self.__decode_sequence(np.argmax(predicted_sequence, axis=-1)[0])
        return predicted_sentence
