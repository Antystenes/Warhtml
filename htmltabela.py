from htmlib import HTML

htmfile = HTML()
lista = open("listaludzi", "r")
htmfile.load("listaludzi.html", "Tabela")
htmfile.f.write("<center>")
htmfile.begintable(2, 25, "FF00FF")

for i in range(25):
    htmfile.rowbegin()
    htmfile.colbegin()
    for j in range(5):
        htmfile.writeln(lista.readline())
    lista.readline()
    htmfile.colend()
    htmfile.colbegin()
    for j in range(5):
        htmfile.writeln(lista.readline())
    lista.readline()
    htmfile.colend()
    htmfile.rowend()
htmfile.f.write("</center>")



htmfile.endtable()
htmfile.closefile()
lista.close()
