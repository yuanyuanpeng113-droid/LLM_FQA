from content.diff_methods import main_prompt
from content.model_API import model_run
from content.evalution import main_evalution_fill, main_evalution_choice, main_evalution_multi_choice
import time
from collections import Counter

def main_ensemble(response1, response2, response3):
    response1 = response1.split('<option>')[1]
    response1 = response1.split('</option>')[0]
    response2 = response2.split('<option>')[1]
    response2 = response2.split('</option>')[0]
    response3 = response3.split('<option>')[1]
    response3 = response3.split('</option>')[0]
    if "# The selected options, e.g., [A] or [C]." in response1:
        response1 = response1.split('# The selected options, e.g., [A] or [C].')[1]
    if "# The selected options, e.g., [A] or [C]." in response2:
        response2 = response2.split('# The selected options, e.g., [A] or [C].')[1]
    if "# The selected options, e.g., [A] or [C]." in response3:
        response3 = response3.split('# The selected options, e.g., [A] or [C].')[1]
    if "# 选择的选项，例如，[BE] 或者 [ACD]，不要提供任何解释." in response1:
        response1 = response1.split('# 选择的选项，例如，[BE] 或者 [ACD].')[1]
    if "# 选择的选项，例如，[BE] 或者 [ACD]，不要提供任何解释." in response2:
        response2 = response2.split('# 选择的选项，例如，[BE] 或者 [ACD].')[1]
    if "# 选择的选项，例如，[BE] 或者 [ACD]，不要提供任何解释." in response3:
        response3 = response3.split('# 选择的选项，例如，[BE] 或者 [ACD].')[1]
    if "[" in response1:
        response1 = response1.split('[')[1]
    if "]" in response1:
        response1 = response1.split(']')[0]
    if "[" in response2:
            response2 = response2.split('[')[1]
    if "]" in response2:
        response2 = response2.split(']')[0]
    if "[" in response3:
        response3 = response3.split('[')[1]
    if "]" in response3:
        response3 = response3.split(']')[0]
    response1_list = list(response1)
    response2_list = list(response2)
    response3_list = list(response3)
    all_response = response1_list + response2_list + response3_list
    # 使用Counter统计每个选项的出现次数
    response_count = Counter(all_response)
    most_response = [choice for choice, count in response_count.items() if count >= 2]
    if len(most_response) == 0:
        most_response = response2_list
    return most_response

def run_main_type(task_type, method, question, model_name, answer):
    if method == "Ensemble":
        prompt = question
        prompt1, prompt2, prompt3 = main_prompt(task_type, method, question)
        response1 = model_run(model_name, prompt1)
        response2 = model_run(model_name, prompt2)
        response3 = model_run(model_name, prompt3)
        response = main_ensemble(response1, response2, response3)
        print('===========================================')
        print("-----------------response1-----------------")
        print(response1)
        print("-----------------response2-----------------")
        print(response2)
        print("-----------------response3-----------------")
        print(response3)
        print('===========================================')
  
    else:
        prompt = main_prompt(task_type, method, question)
        response = model_run(model_name, prompt)
        response = response.split('<option>')[1]
        response = response.split('</option>')[0]
        if "# The selected options, e.g., [A] or [C]." in response:
            response = response.split('# The selected options, e.g., [A] or [C].')[1]
        if "# 选择的选项，例如，[BE] 或者 [ACD]." in response:
            response = response.split('# 选择的选项，例如，[BE] 或者 [ACD].')[1]
        if "[" in response:
            response = response.split('[')[1]
        if "]" in response:
            response = response.split(']')[0]
        
    if task_type == "ch_fill_ques" or task_type == "en_fill_ques":
        output = main_evalution_fill(response, answer)
    elif task_type == "ch_single_choice_ques" or task_type == "en_single_choice_ques":
        output = main_evalution_choice(response, answer)
    elif task_type == "ch_multi_choice_ques" or task_type == "en_multi_choice_ques":
        output = main_evalution_multi_choice(response, answer)
    return prompt, response, output

def main_type(task_type, method, question, model_name, answer):
    time_total = 0
    while True:
        try:
           prompt, response, output = run_main_type(task_type, method, question, model_name, answer)
           break
        except Exception as e:
            time.sleep(20)
            time_total = time_total + 1
            if time_total>5:
                output = 0
                response = ""
                prompt = question
                break

    return prompt, response, output
        
        