import openai
openai.api_key = "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"


def call_openai(prompt, max_tokens=1200):


    
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            # stop=["<h"]
        )

    return response.get("choices")[0]['text']

data = """I want you to act as a travel guide. I will provide the travelling locations and their characteristics inide the triple backticks. 
each row consists with the destination name and it's desctiprtion.

```
Destination,Description
Adam's Peak,"Mountain, Religiuos, Climbing, Steep"
Yala National Park,"National Park, Wildlife, leopards, elephants"
Abalangoda Beach,"Sandy Beach, Masks, Handlooms, Batics"
Arugam Bay,"Beach, Fishing Village, Water Sports, Surfing, Underwater Photography"
Batticaloa Beach,"Beach, Picturesque lagoon, Duth Fort"
Bundala,"National Park, Wildlife, Sea turttles, Birds"
Pinnawala Orphanage,"Elephants, Disabled Elephnats, Elephant Lover"
```

Recommend some travel destination based on the below requirements. Please select locations from the above location details only
Please provide only the travel location list and please do not provide any description about the travel destinations 

'I need to spend some time with elephants'"""

def get_destination(prompt=data):
    return call_openai(prompt)
    