import re

def main_evalution_fill(response, answer):
    matches = re.findall(r'\[(.*?)\]', response)
    if not matches:
        output = 0
        return output
    if matches[0] == answer:
        output = 1
    else:
        output = 0
    return output
def main_evalution_choice(response,answer):
    
    if answer in response:
        output = 1
    else:
        output = 0
    return output

def main_evalution_multi_choice(response, answer):
    
    answer = list(answer)
    result = all(char in response for char in answer)
    if result: 
        response = list(response)
        result1 = all(char in answer for char in response)
        if result1:
            output = 1
        else:
            output = 0
    else:
        output = 0
    return output