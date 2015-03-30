from htmlib import HTML

htmfile = HTML()
lista = open("listaludzi", "r")
htmfile.load("listaludzi.html", "Tabela")

htmfile.f.write('<p style="align:center;">')
htmfile.begintable('style="background-color:magenta;width:25%;border:3px solid black"')
for i in range(25):
    htmfile.rowbegin()
    htmfile.colbegin('style="border:1px solid black"')
    for j in range(5):
        if j==0:
            htmfile.f.write('<p style="color:green;text-align:right">')
        elif j==2:
            htmfile.f.write('</p>')
        htmfile.writeln(lista.readline())
    lista.readline()
    htmfile.colend()
    htmfile.colbegin('style="border:1px solid black"')
    for j in range(5):
        if j==0:
            htmfile.f.write('<p style="color:green;text-align:right">')
        elif j==2:
            htmfile.f.write('</p>')
        htmfile.writeln(lista.readline())

    lista.readline()
    htmfile.colend()
    htmfile.rowend()
htmfile.f.write("</p>")



htmfile.endtable()
htmfile.closefile()
lista.close()
