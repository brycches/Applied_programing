from django.http import HttpResponse


def index(request):
    # return HttpResponse("""Hello, world. You're at the tutor index.
    #                     <head>
    #                         <title>
    #                             This is a tittle
    #                         </title>    
    #                     </head>
    #                     <body>

    #                     </body>""")

    PATH = 'weaknesses/weaknesses.html'

    with open(PATH, 'r') as file:
        return HttpResponse(file)