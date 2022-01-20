class Student:
    def __init__(self,surname,name,patronimyc,booknumber,grade):
        self.surname = surname
        self.name = name
        self.patronimyc = patronimyc
        self.number = booknumber
        self.grade=grade
    def se(self):
        return sum(self.grade)/len(self.grade)
    def pri(self):
        print(f'{self.surname} {self.name} {self.patronimyc}  -  {self.se()}' )
class Group:
    def add(self):
        first=Student('Zohaib','John','Houghton',321,[1,5,2,5])
        first.pri()
        second=Student('Allen','Farrah','Court',245,[4,4,3,5])
        second.pri()
        third = Student('Collins', 'Priyanka', 'James', 677, [5, 4, 3, 5])
        third.pri()
        fours = Student('Ivor', 'Hollis', 'Patrick', 121, [5, 5, 3, 5])
        fours.pri()
        fifth = Student('Wickens', 'Haniya', 'Jaret', 248, [5, 5, 5, 5])
        fifth.pri()