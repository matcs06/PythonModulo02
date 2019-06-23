
from flask import Flask, render_template
from lib import DadosAbertos

app = Flask(__name__)

'''Página inicial'''
@app.route("/")
def inicar():
   return render_template('startPage.html')

'''Listando quantidade de deputados eleitos por estado'''
@app.route("/estado")
def estado():
   obj  = DadosAbertos()
   list_dep = obj.deputados()
   title = "Deputados eleitos por Estado"

   estados = {}

   for dep in list_dep:
       uf = dep['siglaUf']
       if uf in estados:
             estados[uf] += 1
       else:
          estados[uf] =  1
      
   bar_labels=estados.keys()
   bar_values=estados.values()

   return render_template('index.html', max=100, labels=bar_labels, values=bar_values, texto=title)


''' Listando quantidade deputados eleitos por partido'''
@app.route("/partido")
def partido():
   obj  = DadosAbertos()
   list_dep = obj.deputados()
   title = "Deputados eleitos por partido"

   estados = {}

   for dep in list_dep:
       uf = dep['siglaPartido']
       if uf in estados:
             estados[uf] += 1
       else:
          estados[uf] =  1
      
   bar_labels=estados.keys()
   bar_values=estados.values()

   return render_template('index.html', max=100, labels=bar_labels, values=bar_values, texto=title)
   
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)