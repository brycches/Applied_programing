from django import render
import sentence_generator

def display_sentence(request):
    sentence = sentence_generator.make_sentence()
    return render(request, 'your_template.html', {'sentence': sentence})