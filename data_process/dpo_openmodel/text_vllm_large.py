from vllm import LLM, SamplingParams

class VllmModel:
    """open model for answer generate
    """
    def __init__(self, model_path="/mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints/Meta-Llama-3.1-8B-Instruct") -> None:
        """_summary_

        Args:
            model_name (str): model name
            model_path (str, optional): model save path. Defaults to "/mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints".
            max_tokens (int, optional): max generated tokens. Defaults to 2048.
            temperature (float, optional): temperature. Defaults to 0.8.
        """
        self.llm = LLM(model=model_path, tensor_parallel_size=8)
        # gen_kwargs_vllm = {
        #     "max_tokens": max_tokens,
        #     "top_p":0.9,
        #     "temperature": temperature,
        #     "top_k":50,
        #     "repetition_penalty": 1.0
        # }
        # self.gen_kwargs_vllm = {}
        template = "{% if messages[0]['role'] == 'system' %}{% set system_message = messages[0]['content'] %}{% endif %}{% if system_message is defined %}{{ system_message + '\n' }}{% endif %}{% for message in messages %}{% set content = message['content'] %}{% if message['role'] == 'user' %}{{ 'Human: ' + content + '\nAssistant:' }}{% elif message['role'] == 'assistant' %}{{ content + '<|end_of_text|>' + '\n' }}{% endif %}{% endfor %}"
        self.tokenizer = self.llm.get_tokenizer()
        if self.tokenizer.chat_template is None:
            self.tokenizer.chat_template = template
            self.stop_token_ids = [self.tokenizer.eos_token_id, self.tokenizer.convert_tokens_to_ids("<|eot_id|>")]
            print(f"tokenizer.chat_template: {self.tokenizer.chat_template}")
            print("tokenizer is None, use setted template")
        else:
            self.stop_token_ids = [self.tokenizer.eos_token_id, self.tokenizer.convert_tokens_to_ids("<|end_of_text|>")]
            print("use original template")


    def batch_generate(self, messages, image_sources=None, temperature=0.7, max_tokens=2048, top_p=0.95, repetition_penalty=1.05):  
        gen_kwargs_vllm = {
            "max_tokens": max_tokens,
            "top_p": top_p,
            "temperature": temperature,
            "repetition_penalty": repetition_penalty,
            "top_k":50,
            "stop_token_ids": self.stop_token_ids

        }
        sampling_params = SamplingParams(**gen_kwargs_vllm)

        # messages = [[{"role": "user", "content": input}] for input in messages]  
        inputs = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        encoded_inputs = self.tokenizer.batch_encode_plus(  
            inputs,  
            add_special_tokens=False,
        ) 
        input_ids = encoded_inputs['input_ids'] 
        outputs = self.llm.generate(prompt_token_ids=input_ids, sampling_params=sampling_params)
        outputs_text = [x.outputs[0].text for x in outputs]
        stop_reasons = [output.outputs[0].finish_reason for output in outputs]
        return outputs_text, stop_reasons
                                
if __name__ == '__main__':
    model = VllmModel("/mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints/Meta-Llama-3.1-8B-Instruct")
    messages_1 = [  
        {  
            "role": "user",  
            "content": "hello"  
        }  
    ]  
    messages_2 = [  
        {  
            "role": "user",  
            "content": "Who are you?"  
        }  
    ]
    input_x = [messages_1, messages_2]
    text = model.batch_generate(input_x)
    print(text)