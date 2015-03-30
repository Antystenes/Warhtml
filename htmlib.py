class HTML:
    headings = 1
    def load(self, filename, title = " " ):
        self.f = open(filename, 'w')
        self.f.write("<!DOCTYPE html>")
        self.f.write("<html>")
        self.f.write("<head>")
        self.f.write('  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8" >')
        self.f.write("  <title>"+title+"</title>")
        self.f.write("</head>")
        self.f.write("\n<body>")

    def closefile(self):
        self.f.write("</body>")
        self.f.write("</html>")
        self.f.close()
    
    def paragraph(self, text):
        self.f.write("<p>"+text+"</p>")

    def heading(self, text):
        self.f.write("<h"+str(headings)+">"+text+"</h"+headings+">")
        heading += 1
        
    def begintable(self, border = 1, width = 100, bgcolor = 'white'):
        self.f.write('<table border="'+str(border)+'" style="width:'+str(width)+'%" bgcolor="#'+bgcolor+'">')

    def endtable(self):
        self.f.write("</table>")
    
    def writeln(self, text):
        self.f.write(text+"<br>")
        
    def write(self, text):
        self.f.write(text+"<br>")
        
    def rowbegin(self):
        self.f.write("<tr>")
        
    def rowend(self):
        self.f.write("</tr>")

    def colbegin(self):
        self.f.write("<td>")

    def colend(self):
        self.f.write("</td>")

