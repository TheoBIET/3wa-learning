class Message:
    def __init__(self, text):
        self.text = text

    def __contains__(self, word):
        return word in self.text

class FormattedMessage(Message):
    def __contains__(self, word):
        return word.upper() in self.text.upper()

test = FormattedMessage("Hello world")
print(test.contains("hello"))