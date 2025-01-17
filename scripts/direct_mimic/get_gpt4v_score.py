import json  
import re  
  
def extract_scores(response_text):  
    scores = {  
        "chart_types_score": 0,  
        "layout_score": 0,  
        "text_content_score": 0,  
        "data_score": 0,  
        "style_score": 0,  
        "clarity_score": 0,  
        "gpt4v_score": 0.0  
    }  
      
    # Regex patterns to extract scores  
    patterns = {  
        "chart_types_score": r"Chart Types:.*?Score: (\d+)\/20",  
        "layout_score": r"Layout:.*?Score: (\d+)\/10",  
        "text_content_score": r"Text Content:.*?Score: (\d+)\/20",  
        "data_score": r"Data:.*?Score: (\d+)\/20",  
        "style_score": r"Style:.*?Score: (\d+)\/20",  
        "clarity_score": r"Clarity:.*?Score: (\d+)\/10",  
        # Make the score extraction case-insensitive  
        "gpt4v_score": r"(?:S|s)core: (\d+)\/100"  
    }  
      
    # Extract scores using regex  
    for key, pattern in patterns.items():  
        match = re.search(pattern, response_text, re.IGNORECASE if key == "gpt4v_score" else 0)  
        if match:  
            if key == "gpt4v_score":  
                scores[key] = int(match.group(1)) / 100.0  # Convert to decimal  
            else:  
                scores[key] = int(match.group(1))  # Keep as integer  
      
    return scores  
  
def process_jsonl_file(input_file, output_file):  
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:  
        for line in infile:  
            entry = json.loads(line)  
            response = entry.get("response", "")  
            scores = extract_scores(response)  
            entry.update(scores)  
            outfile.write(json.dumps(entry, ensure_ascii=False) + '\n')  
  
# Example usage  
input_file = 'results/gpt4evaluation_gpt-4o_GPT4EvaluationAgent_direct_results.json'  
output_file = 'results/gpt4evaluation_gpt-4o_GPT4EvaluationAgent_direct_results.json'  
process_jsonl_file(input_file, output_file)  