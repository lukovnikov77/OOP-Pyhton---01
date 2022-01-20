
class FileAnylizer:

    def __init__(self, path):
        self.path = path

    def words_count(self):
        with open(self.path) as file:
            data = file.read()
            words = data.split()
            return len(words)

    def chars_count(self):
        with open(self.path) as file:
            data = file.read()
            return len(data)

    
file_to_anylize = FileAnylizer("sample.txt");

print("characters:", file_to_anylize.chars_count());
print("words:", file_to_anylize.words_count());
