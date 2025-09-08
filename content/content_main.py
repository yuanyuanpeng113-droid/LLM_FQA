from content.data_handle import read_choice, read_fill, write_jsonl
from content.content_type import main_type

def main_fill(task_type, method, model_name, input_file_path):   
    data = read_fill(input_file_path)
    data_len = len(data)
    response_list = []
    total = 0
    for idx in range(data_len):
        question = data[idx]['question']
        answer = data[idx]['answer'][0]
        ques_id = data[idx]['id']
        prompt, response, output = main_type(task_type, method, question, model_name, answer)
        total = total + int(output)
        res = total/(idx + 1)*100
        res = round(res, 2)
        print('-----------------------------')
        print(f"第{idx}个填空题题目为:\n<<{question}>>,\n{model_name}的输出结果为:<<{response}>>,\n正确的答案为:<<{answer}>>,\n当前总体结果的正确率为: {res}%")
        
        response_list.append(dict({"id": ques_id, "response": response, "answer": answer, "result": output}))
    return response_list

def main_choice(task_type, method, model_name, input_file_path):
    data = read_choice(input_file_path)
    data_len = len(data)
    total = 0
    response_list = []
    
    for idx in range(data_len):
        ques_id = data[idx]['id']
        question = data[idx]['question']
        choice_A = data[idx]['options'][0]['option']
        choice_A_content = data[idx]['options'][0]['content']
        choice_B = data[idx]['options'][1]['option']
        choice_B_content = data[idx]['options'][1]['content']
        choice_C = data[idx]['options'][2]['option']
        choice_C_content = data[idx]['options'][2]['content']
        answer = data[idx]['answer']
        domain = data[idx]['domain']
        level = data[idx]['difficulty level']
        try:
            choice_D = data[idx]['options'][3]['option']
            choice_D_content = data[idx]['options'][3]['content']
            problem = question + "\n" + choice_A + "." + choice_A_content + "\n" + choice_B + "." + choice_B_content + "\n" + choice_C + "." + choice_C_content + "\n" + choice_D + "." + choice_D_content + "\n"
            prompt, response, output = main_type(task_type, method, problem, model_name, answer)
            total = total + int(output)
            res = total/(idx + 1)*100
            res = round(res, 2)
            print('-----------------------------')
            print(f"第{idx}个选择题题目为:\n{problem}\n{model_name}的输出结果为:<<{response}>>,\n正确的答案为:<<{answer}>>,\n当前总体结果的正确率为: {res}%")
            response_list.append(dict({"id": ques_id, "response": response, "answer": answer, "result": output}))
        except:
            problem = question + "\n" + choice_A + "." + choice_A_content + "\n" + choice_B + "." + choice_B_content + "\n" + choice_C + "." + choice_C_content + "\n"
            question_forward = question
            # prompt = "从下来问题中选择一个正确的选择，并且重要的是你必须选择正确选项的字母\n" + problem
            prompt, response, output = main_type(task_type, method, problem, model_name, answer)
            total = total + int(output)
            res = total/(idx + 1)*100
            res = round(res, 2)
            print('-----------------------------')
            print(f"第{idx}个选择题题目为:\n{problem}\n{model_name}的输出结果为:<<{response}>>,\n正确的答案为:<<{answer}>>,\n当前总体结果的正确率为: {res}%")
            response_list.append(dict({"id": ques_id, "response": response, "answer": answer, "result": output}))
    return response_list

def main_multi_choice(task_type, method, model_name, input_file_path):
    data = read_choice(input_file_path)
    data_len = len(data)
    total = 0
    response_list = []
    for idx in range(data_len):
        ques_id = data[idx]['id']
        question = data[idx]['question']
        options = data[idx]['options']
        options_len = len(options)
        answer = data[idx]['answer']
        if options_len == 3:
            choice_A = options[0]['option']
            choice_A_content = options[0]['content']
            choice_B = options[1]['option']
            choice_B_content = options[1]['content']
            choice_C = options[2]['option']
            choice_C_content = options[2]['content']
            problem = question + "\n" + choice_A + "." + choice_A_content + "\n" + choice_B + "." + choice_B_content + "\n" + choice_C + "." + choice_C_content + "\n"
        elif options_len == 4:
            choice_A = options[0]['option']
            choice_A_content = options[0]['content']
            choice_B = options[1]['option']
            choice_B_content = options[1]['content']
            choice_C = options[2]['option']
            choice_C_content = options[2]['content']
            choice_D = options[3]['option']
            choice_D_content = options[3]['content']
            problem = question + "\n" + choice_A + "." + choice_A_content + "\n" + choice_B + "." + choice_B_content + "\n" + choice_C + "." + choice_C_content + "\n" + choice_D + "." + choice_D_content + "\n"
        elif options_len == 5:
            choice_A = options[0]['option']
            choice_A_content = options[0]['content']
            choice_B = options[1]['option']
            choice_B_content = options[1]['content']
            choice_C = options[2]['option']
            choice_C_content = options[2]['content']
            choice_D = options[3]['option']
            choice_D_content = options[3]['content']
            choice_E = options[4]['option']
            choice_E_content = options[4]['content']
            problem = question + "\n" + choice_A + "." + choice_A_content + "\n" + choice_B + "." + choice_B_content + "\n" + choice_C + "." + choice_C_content + "\n" + choice_D + "." + choice_D_content + "\n" + choice_E + "." + choice_E_content + "\n"
        elif options_len == 6:
            choice_A = options[0]['option']
            choice_A_content = options[0]['content']
            choice_B = options[1]['option']
            choice_B_content = options[1]['content']
            choice_C = options[2]['option']
            choice_C_content = options[2]['content']
            choice_D = options[3]['option']
            choice_D_content = options[3]['content']
            choice_E = options[4]['option']
            choice_E_content = options[4]['content']
            choice_F = options[5]['option']
            choice_F_content = options[5]['content']
            problem = question + "\n" + choice_A + "." + choice_A_content + "\n" + choice_B + "." + choice_B_content + "\n" + choice_C + "." + choice_C_content + "\n" + choice_D + "." + choice_D_content + "\n" + choice_E + "." + choice_E_content + "\n" + choice_F + "." + choice_F_content + "\n"
        print('----------------------------------')
        prompt, response, output = main_type(task_type, method, problem, model_name, answer)
        total = total + int(output)
        res = total/(idx + 1)*100
        res = round(res, 2)
        print('-----------------------------')
        print(f"第{idx}个选择题题目为:\n{problem}\n{model_name}的输出结果为:<<{response}>>,\n正确的答案为:<<{answer}>>,\n当前总体结果的正确率为: {res}%")
        response_list.append(dict({"id": ques_id, "response": response, "answer": answer, "result": output}))
    return response_list

def main(method, task_type, model_name, save_path):
    
    # 中文填空
    if task_type == "ch_fill_ques":
        input_file_path = "/home/wangshuai/main_dirfile/LLM_Q_A/large_model_test/data/ch_fill_ques.json"
        response = main_fill(task_type, method, model_name, input_file_path)
    # 中文单选
    elif task_type == "ch_single_choice_ques":
        input_file_path = '/home/wangshuai/main_dirfile/LLM_Q_A/large_model_test/data/ch_single_choice_ques.json'
        response = main_choice(task_type, method, model_name, input_file_path)
    # 中文多选    
    elif task_type == "ch_multi_choice_ques":
        input_file_path = '/home/wangshuai/main_dirfile/LLM_Q_A/large_model_test/data/ch_multi_choice_ques.json'
        response = main_multi_choice(task_type, method, model_name, input_file_path)
    # 英文填空
    elif task_type == "en_fill_ques":
        input_file_path = "/home/wangshuai/main_dirfile/LLM_Q_A/large_model_test/data/en_single_fill_ques.json"
        response = main_fill(task_type, method, model_name, input_file_path)
    # 英文单选
    elif task_type == "en_single_choice_ques":
        input_file_path = '/home/wangshuai/main_dirfile/LLM_Q_A/large_model_test/data/en_single_choice_ques.json'
        response = main_choice(task_type, method, model_name, input_file_path)
    # 英文多选
    elif task_type == "en_multi_choice_ques":
        input_file_path = '/home/wangshuai/main_dirfile/LLM_Q_A/large_model_test/data/en_multi_choice_ques.json'
        response = main_multi_choice(task_type, method, model_name, input_file_path)
    write_jsonl(save_path, response)