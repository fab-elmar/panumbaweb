import os
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re


from django.http import JsonResponse

from openai import OpenAI
from asgiref.sync import sync_to_async

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import AIcontact
from django.views import View

import logging
logger = logging.getLogger(__name__)



# @method_decorator(login_required, name='dispatch')
class AIcontactListView(ListView):
    model = AIcontact
    template_name = "interface/panumba_list.html"
    context_object_name = "AIcontacts"
    ordering = ["id"]
   
    queryset = AIcontact.objects.all()


@method_decorator(login_required, name='dispatch')
class PanumbaQuestionView(View):
    template_name = "interface/question_template.html"
    def get(self, request, *args, **kwargs):
        # Handle GET request
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        openai_api_key = os.environ.get('OPENAI_API_KEY')
        
        # Handle POST request
        user_question = request.POST.get('question')
        logger.info('User question: %s', user_question)
        
        if openai_api_key is None:
            logger.error("OpenAI API key is not set.")
           
            return render(request, self.template_name, {'error': 'API key not set.'})
        client = OpenAI(api_key=openai_api_key)
        MODEL = "gpt-3.5-turbo"
        # INSTRUCTION = "Provide an answer in two parts the answer should have to key value paiars. The first key 'number' should have an integer as value that is logically associated with the question or in case there is the direct answer. The second part, under the key 'context', should be a brief explanation of the logic used to derive the number. For direct questions like 'How many days are in a week?', return the factual answer. For abstract questions like 'What color is the sky?', derive a number using a logical method and explain this method in the context." 
        modifyed_instruction = "Provide an answer in two parts: the answer should have two key-value pairs both enclosed in double quotes pairs. The format must be parseable as json. The first key 'number' must have  an integer as value written out in full with all trailing zeros (e.g., 4,500,000 for 4.5 million) as the value that is logically associated with the question or, pleae set the integer in double quotes. The second part, under the key 'context', should be a brief explanation of the logic used to derive the integer number. For direct questions like 'How many days are in a week?', return the factual answer as an integer. For abstract questions like 'What is the age of the sea?' or 'What color is the sky?' always give an integer using a logical method of your choice and explain this method in the context. Please try to be creative and have fun, the numbers should be as interesting as possible. Try to avoid one digit answers. If the question involves speculation and uncertainty please provide an integer based on that."

        responses = []
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": modifyed_instruction  },
                {"role": "user", "content": user_question},
            
            ],
            temperature=0,
        )
        content = response.choices[0].message.content
        
        logger.info('Response: %s', response)
        logger.info('Response choices: %s',   content)
        
       
        # Replace escaped single quotes and backslashes
        content = content.replace("'", "\\'").replace("\\", "\\\\")

        # Remove commas from numbers
        content = re.sub(r'(\d),(\d)', r'\1\2', content)
        try:
            response_content = json.loads(content)
        except json.JSONDecodeError as e:
            logger.info(f"Error parsing JSON content: {e}")
            return render(request, self.template_name, {'context': 'Invalid response format.'})
        

        # Extract 'number' and 'context' values
        number = response_content.get('number')
        context = response_content.get('context')
        
        if isinstance(number, str):
            number = int(number.replace(',', ''))
        
        number = int(number)
        logger.info('Number: %s', number)
       
        
        response_data = {
            "question": user_question,
            "number": number,
            "context": context
        }
        logger.info('Response data: %s', response_data)
        username = request.user.username if request.user.is_authenticated else 'Guest'
        AIcontact.objects.create(name=username, question=user_question, answer=number, context=context)
        
        
        

        
        return render(request, self.template_name, {'context': context})
    
    
    
    

class ShowNumberView(View):
    template_name = 'interface/show_number.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
    
    



class WorldPopulationView(View):
    def get(self, request, *args, **kwargs):
       
        url = 'https://www.worldometers.info'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        bicycle_div = soup.select_one('div.counter-heading[data-target="#bicycle_produced"]')        
        if bicycle_div:
            bicycle_count = ''.join([span.get_text() for span in bicycle_div.find_all('span', class_='rts-nr-int')])
        else:
            bicycle_count = 'Data not found'
            
        logger.info('World Bici: %s', bicycle_count)
        return JsonResponse({'bicycle_count': bicycle_count})