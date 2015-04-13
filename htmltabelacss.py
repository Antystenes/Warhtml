from htmlib import HTML

htmfile = HTML()
lista = open("listaludzi", "r")
htmfile.load("listaludzicss.html", "Tabela")

htmfile.begintable()
for i in range(25):
    htmfile.rowbegin()
    htmfile.colbegin()
    for j in range(5):
        if j==0:
            htmfile.f.write('<p class="name">')
        elif j==2:
            htmfile.f.write('</p>')
            htmfile.f.write('<p class="data">')
        elif j==5:
            htmfile.f.write("</p>")
        htmfile.writeln(lista.readline())
    lista.readline()
    htmfile.colend()
    htmfile.colbegin()
    for j in range(5):
        if j==0:
            htmfile.f.write('<p class="name">')
        elif j==2:
            htmfile.f.write('</p>')
            htmfile.f.write('<p class="data">')
        elif j==5:
            htmfile.f.write("</p>")
        htmfile.writeln(lista.readline())

    lista.readline()
    htmfile.colend()
    htmfile.rowend()



htmfile.endtable()
htmfile.closefile()
lista.close()
