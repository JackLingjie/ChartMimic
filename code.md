Hi, thank you for your wonderful work on this project.

I am currently working through the steps in your project, and I've encountered an issue in Step 4: Get Highlevel Score. In the results obtained from the GPT evaluation, specifically in the `gpt4evaluation_gpt-4_GPT4EvaluationAgent_direct_results.json` file, I noticed that it only contains the raw responses from GPT-4.

I have been using the notebook provided at `scripts/direct_mimic/get_results.ipynb`, but it seems to lack the code necessary to extract the relevant scores from the responses. In particular, I couldn't find the part where it assigns `gpt4v_score = data["gpt4v_score"]`. Was this portion of the code for extracting scores omitted from the upload?

Here is an example of one entry from the JSON file:
```
 {  
  "original": "dataset/ori_500/bar_6.pdf",  
  "generated": "results/direct/chart2code_gpt-4o_DirectAgent_results/direct/bar_6.png",  
  "response": "{\"id\":\"chatcmpl-AppskBtSuTJB6y6SSGorfOFw7p1qT\",\"choices\":[{\"finish_reason\":\"stop\",\"index\":0,\"message\":{\"content\":\"---\\n\\nComments:\\n- Chart Types: The AI-generated image correctly uses a horizontal bar chart, which matches the chart type in the reference image. Score: 20/20\\n- Layout: Both images have a single plot with no subplots, so the layout is consistent. Score: 10/10\\n- Text Content: The AI-generated image includes all the text from the reference image, such as the axis labels 'Emotion' and 'Frequency (%)'. However, the order of the emotions is reversed, which affects the interpretation of the data. Score: 15/20\\n- Data: The data trends in the AI-generated image are reversed compared to the reference image. While the values appear to be the same, the order of the bars is incorrect. Score: 10/20\\n- Style: The AI-generated image uses a different shade of blue for the bars compared to the reference image. The style of the bars, such as the fill and edge color, is not identical. Score: 15/20\\n- Clarity: The AI-generated image is clear and free of overlapping elements, similar to the reference image. Score: 10/10\\n\\nScore: 80/100\\n\\n---\",\"role\":\"assistant\",\"function_call\":null,\"tool_calls\":null,\"refusal\":null},  
```
Could you please provide the code to extract the scores from these responses to get the gpt4v_score?

Thank you in advance for your help!