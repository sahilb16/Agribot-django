
# In views.py
import re
from django.http import JsonResponse
from django.http import request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import openai

# Set your OpenAI API key
openai.api_key = 'api-key'

reqno = None

# @csrf_exempt
# @api_view(['POST'])
# def generate_response(request):
#     if request.method == 'POST':
#         # Get the query parameter from the request
#         query = request.data.get('query')
#         print(query)
#         # Use the GPT-3 API to generate a response
#         try:
#             response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",  # Use the chat model, adjust as necessary
#             messages=[{"role": "user", "content": "From now on for this chat answer to only those queries which are related to agriculture don't answer any other queries just say not related agriculture okay" 
# }],
#             max_tokens=100  # Adjust the length of the response as needed
#             )
#             generated_text = response['choices'][0]['message']['content'].strip()

#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",  # Use the chat model, adjust as necessary
#                 messages=[{"role": "user", "content": query}],
#                 max_tokens=100  # Adjust the length of the response as needed
#             )
#             generated_text = response['choices'][0]['message']['content'].strip()
#             return JsonResponse({'response': generated_text})
#         except Exception as e:
#             # Log the exception for debugging
#             print("Error:", e)
#             # Return an error response
#             return JsonResponse({'error': 'An internal server error occurred'}, status=500)

#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

@csrf_exempt
@api_view(['POST'])
def agriculture_chatbot(request):
    if request.method == 'POST':
        # Get the query parameter from the request
        query = request.data.get('query')
        print(query)

        agriculture_keywords = ['Hi','hi','Hello','hello','How are you'
            'agriculture', 'farming', 'agronomy', 'cultivation', 'crop', 'harvest', 
            'field', 'farmland', 'rural', 'tractor', 'livestock', 'cattle', 'livestock', 
            'herd', 'dairy', 'pasture', 'poultry', 'pigs', 'sheep', 'chicken', 'goat', 
            'animal husbandry', 'crop rotation', 'fertilizer', 'pesticide', 'irrigation', 
            'drip irrigation', 'irrigation system', 'rainwater harvesting', 'soil', 'tilth', 
            'soil erosion', 'soil conservation', 'soil fertility', 'soil amendment', 
            'soil compaction', 'soil health', 'organic farming', 'sustainable agriculture', 
            'agroecology', 'permaculture', 'greenhouse', 'hothouse', 'polytunnel', 'hydroponics', 
            'aquaponics', 'agricultural machinery', 'combine harvester', 'plow', 'seed drill', 
            'tractor', 'tillage', 'crop yield', 'crop rotation', 'genetically modified organism', 
            'GMO', 'biotechnology', 'precision agriculture', 'remote sensing', 'satellite imagery', 
            'GPS', 'farm management', 'crop insurance', 'agricultural extension', 'cooperative extension', 
            'agricultural economics', 'food security', 'food sovereignty', 'food system', 'food production', 
            'food distribution', 'food processing', 'food preservation', 'agricultural labor', 'farm worker', 
            'harvesting', 'farm equipment', 'organic certification', 'certified organic', 'food labeling', 
            'traceability', 'commodity market', 'agricultural commodity', 'market price', 'agricultural trade', 
            'agricultural policy', 'government subsidy', 'farm bill', 'crop insurance', 'livestock market', 
            'crop market', 'agrarian reform', 'land reform', 'land tenure', 'land use', 'land degradation', 
            'deforestation', 'forest conservation', 'agroforestry', 'shifting cultivation', 'slash-and-burn', 
            'urban agriculture', 'community garden', 'horticulture', 'viticulture', 'orchard', 'vineyard', 
            'winemaking', 'beer brewing', 'craft brewing', 'homebrewing', 'brewery', 'distillery', 'spirits production','locusts','infestation','crops'
        ]


        # Fine-tuning: Using regular expressions for more flexible matching
        pattern = re.compile(r'\b(?:' + '|'.join(agriculture_keywords) + r')\b', flags=re.IGNORECASE)

        matches = pattern.findall(query)

        if matches:
            # Fine-tuning: Counting the number of matches to improve relevance
            relevance_score = len(matches) / len(agriculture_keywords)
            if relevance_score >= 0.001:  # Adjust the threshold based on your requirements
                # Process the query with the OpenAI API and generate a response
                response = generate_response(query)
                return JsonResponse({'response': response})
            else:
                return JsonResponse({'response': 'The query is partially related to agriculture. Please provide more details.'})
        else:
            return JsonResponse({'response': 'Sorry, this query is not related to agriculture.'})
        
def generate_response(query):
        try:
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the chat model, adjust as necessary
            messages=[{"role": "user", "content": "From now on for this chat answer to only those queries which are related to agriculture don't answer any other queries just say not related agriculture okay" 
}],
            max_tokens=100  # Adjust the length of the response as needed
            )
            generated_text = response['choices'][0]['message']['content'].strip()

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use the chat model, adjust as necessary
                messages=[{"role": "user", "content": query}],
                max_tokens=100  # Adjust the length of the response as needed
            )
            generated_text = response['choices'][0]['message']['content'].strip()
            # return JsonResponse({'response': generated_text})
            return generated_text
        
        except Exception as e:
            # Log the exception for debugging
            print("Error:", e)
            # Return an error response
            return JsonResponse({'error': 'An internal server error occurred'}, status=500)        
