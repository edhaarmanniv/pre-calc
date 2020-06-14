import numpy as np
from random import *

class Question:
    def __init__(self):
        self.correct_coeffs = self.create_coeffs()
        self.options = ["A", "B", "C", "D"]
        self.correct_option = choice(self.options)
        self.correct_choice = {**self.correct_coeffs, "correct":True, "display_string":self.display_abc(self.correct_coeffs)}
        self.all_choices_abc = {self.correct_option:self.correct_choice}
        self.all_choices_hk = dict()
        
    
    def find_h(self, coeffs):
        return -coeffs["b"]/(2*coeffs["a"])
        
    def find_k(self, coeffs):
        h = self.find_h(coeffs)
        return coeffs["a"]*h**2 + coeffs["b"]*h + coeffs["c"]
        
    
    def create_coeffs(self):
        coeffs = list(range(-5, 6, 1))
        coeffs.remove(0)

        a = choice(coeffs)
        b = randint(-5, 5)
        c = randint(-5, 5)

        if b == c and b == min(coeffs):
            c += 1
        if b == c and b == max(coeffs):
            c -= 1

        return {"a": a, "b": b, "c": c}
    
    def create_wrong(self, wr, abc):
        wr.update({abc:self.correct_coeffs[abc]*(-1), "correct":False})
            
    def create_wrong_options(self):
        wr_a = self.correct_coeffs.copy()
        wr_b = self.correct_coeffs.copy()
        wr_c = self.correct_coeffs.copy()
    
        self.create_wrong(wr_a, "a")
        self.create_wrong(wr_b, "b")
        self.create_wrong(wr_c, "c")

        return [
            wr_a,
            wr_b,
            wr_c
        ]

    def display_abc(self, coeffs):
        return r"y=({a})x^2+({b})x+({c})".format(**coeffs)
    
    def display_hk(self, coeffs):
        h = self.find_h(coeffs)
        k = self.find_k(coeffs)
        a = coeffs["a"]
        return fr"y={a}(x-({h}))^2+({k})"
    
    def create_all_options_abc(self):
        
        remaining_options = self.options.copy()
        remaining_options.remove(self.correct_option)
        
        wrong_choices = self.create_wrong_options()
        shuffle(wrong_choices)
        for option, choice in zip(remaining_options, wrong_choices):
            choice.update({"display_string":self.display_abc(choice)})
            self.all_choices_abc.update({option:choice})
        
        return self.all_choices_abc
    
    def create_all_options_hk(self):
        
        for option, coeffs in self.create_all_options_abc().items():
            h = self.find_h(coeffs)
            k = self.find_k(coeffs)
            self.all_choices_hk.update({option:{"h":h, "k":k, "correct":coeffs["correct"], "display_string":self.display_hk(coeffs)}})
        
        return self.all_choices_hk

    def create_question_abc(self):    
        
        question = f"Re-write the following in standard h k form: {self.display_abc(self.correct_coeffs)}"
        options = self.create_all_options_hk()

        return {"question":question,
        "options": options}

    def create_question_hk(self):    
        
        question = f"Re-write the following in a b c form: {self.display_hk(self.correct_coeffs)}"
        options = self.create_all_options_abc()

        return {"question":question,
        "options": options}