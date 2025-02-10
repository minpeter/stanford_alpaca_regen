
<p align="center" width="100%">
<img src="assets/logo.png" alt="Stanford-Alpaca" style="width: 50%; min-width: 300px; display: block; margin: auto;">
</p>

# Stanford Alpaca Regenerate: An Instruction-following LLaMA Model

Updated to the latest OpenAI Python SDK.
For the data generation part, we mostly keep it and instead replace the model training part with axolotl config.

## create dataset

You need a `FRIENDLI_TOKEN`. You can get it from the [document](https://friendli.ai/docs/guides/personal_access_tokens).

```bash
## Generate 52 new data -> regen.json
python -m generate_instruction generate_instruction_following_data \
  --output_dir ./ \
  --num_instructions_to_generate 52

# convert regen.json to jsonl -> output.jsonl
python convert_to_jsonl.py
```

### Example of completed data

```
$ head -n 1 output.jsonl
{"instruction": "What can you infer from the following conversation?", "input": "John: How was your weekend?\nJane: It was great. I went to the beach with friends and had a lot of fun.", "output": "Jane had a great weekend and enjoyed her time at the beach with friends."}
```