from glob_lit import Lit

class OneOrMore:
    def __init__(self, pattern):
        self.pattern = pattern #whatever comes before or after the + sign

    def match(self, text, start=0):
        for i in range(start + 1, len(text) + 1): #minimum one character skipped, and we end before the last
            if self.pattern:    
                if self.pattern.match(text, i):#match function
                    return True
            else:
                if i == len(text):              # ← consumed everything, done
                    return True
        return False