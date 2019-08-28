class Person:
    
    def __init__(self):
        self.name = ""
        self.__inner_thought = "I'm dreaming"
        
    def talk(self):
        print(self.thought);
        
    def __inner_talk(self):
        print(self.__inner_thought)

    def __del__(self):
        print(f"Object {__name__} is destroyed")