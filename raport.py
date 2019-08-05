import os
import codecs
import datetime

now = datetime.datetime.now()
pliki_wejscie = os.listdir("input")
pliki_wyjscie = os.listdir("output")
dane_wejscie = []
dane_wyjscie = []
for i in range(0, len(pliki_wejscie)):
    wejscie = open("input\\" + pliki_wejscie[i], "r")
    wyjscie = open("output\\" + pliki_wyjscie[i], "r")
    dane_wejscie.append(wejscie.read())
    dane_wyjscie.append(wyjscie.read())
    wejscie.close()
    wyjscie.close()
    #print(dane_wejscie)
    #print(dane_wyjscie)
f = codecs.open("raport.html", "w", "utf-8")
f.write("""<!doctype html>
<html>
<head>
<meta charset="UTF-8">
  <title>Obecna edycja</title>
  <link rel="stylesheet" type="text/css" href="https://unpkg.com/purecss@1.0.0/build/tables-min.css">

 
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
<header>
  <div>Raport wygenerowany """ + str(now.strftime("%Y-%m-%d %H:%M")) + """</div>
</header>
 <section>
<h2>Podstawowe działania statystyczne</h2>
 </section>
""")
f.write("""<table class="pure-table pure-table-bordered">
<thead><tr><td>Dane wejściowe</td><td>Wynik</td></tr></thead>
""")
for i in range(len(dane_wejscie)):
    dane1 = dane_wejscie[i]
    dane1 = "<br />".join(dane1.split("\n"))
    dane2 = dane_wyjscie[i]
    dane2 = "<br />".join(dane2.split("\n"))
    f.write("<tr><td>" + dane1 + "</td><td>" + dane2 + "</td></tr>")
    



f.write("</table>")
f.write("<h2>Statystyka dla plików</h2>")
f.write("<p>Ilość przetworznych plików wejściowych : " + str(len(dane_wejscie)) + "</p>")
f.write("<p>Ilość przetworznych plików wyjściowych : " + str(len(dane_wyjscie)) + "</p>")
f.write("</body>")
f.close()
