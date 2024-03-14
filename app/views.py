from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import *
import telebot, random

def home(request):
        return HttpResponse('Salom Dunyo!')

TOKEN = '6596894056:AAFwScLkMoTPzCwB1yNMZENqsR1KGTzgkL4'

bot = telebot.TeleBot(TOKEN)
quiz = Math_Quiz.objects.all()
index = 0
score = 0

@csrf_exempt
def bot_view(request):
    if request.method == 'GET':
        return HttpResponseBadRequest('Bu GET Request')
    elif request.method == 'POST':
        try:
            update = telebot.types.Update.de_json(request.body.decode('utf-8'))
            bot.process_new_updates([update])
            return HttpResponseBadRequest(status=200, content='Bu POST Request')
        except Exception as e:
            print(e)
            
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Math Quiz botga hush kelibsiz!")
    start_quiz(message)

@bot.message_handler(content_types=['text'])
def other_send_message(message):
    global index, quiz, score
    user_answer = message.text
    correct_answer = quiz[index].answer
    
    if user_answer.lower() == correct_answer.lower():
        score += 1
        
    index += 1
    
    if index < 5:
        question = quiz[index]
        bot.send_message(message.chat.id, f'Savolni yeching: {question.question}')
    else:
        bot.send_message(message.chat.id, f"O'yin tugadi! Sizning jami ballingiz: {score}\nQayta boshlash uchun /start ni bosing!")

def get_random_questions():
    questions = list(Math_Quiz.objects.all())
    random.shuffle(questions)
    return questions[:5]

def start_quiz(message):
    global quiz, index, score
    quiz = get_random_questions()
    index = 0
    score = 0
    question = quiz[index]
    bot.send_message(message.chat.id, f'Savolni yeching: {question.question}')