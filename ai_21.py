import ai21
ai21.api_key = '7YDL8mEO3HfTd5b3gWrXo3m8lQwhNeCU'
prompt = """Q: Give a detailed discription of Nepenthes mirabilis  and detail how it is cared for.
A:"""

# J2 Grande
response = ai21.Completion.execute(
  model="j2-jumbo",
  prompt=prompt,
  numResults=1,
  maxTokens=500,
  temperature=0.5,
  topKReturn=0,
  topP=0.5,
  stopSequences=["Q:"]
)

print(prompt + response['completions'][0]['data']['text'])