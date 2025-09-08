import argparse
# from translate import translate_text
from content.content_main import main

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--task_type", type= str, default="choice_ques")
    parser.add_argument("--method", type= str, default="standard")
    parser.add_argument("--model_name", type= str, default="THUDM/chatglm3-6b")
    parser.add_argument("--save_path", type= str, default="F:/code/large_model_test/output_result/yi-large.json")
    arg = parser.parse_args()
    main(arg.method, arg.task_type, arg.model_name, arg.save_path)
    # task_type可以为"ch_fill_ques"，"ch_single_choice_ques", "ch_multi_choice_ques", "en_fill_ques", "en_single_choice_ques", "en_multi_choice_ques"
    # # model_name可以为"deepseek-chat"，"yi-large", "llama3-70b-8192"等
    # model_name = "THUDM/chatglm3-6b"