from flask import Flask, render_template, request, redirect
from requisition import news, comments
import ast


app = Flask('Tech News')

@app.route('/')
def inicial():
  order_by = request.args.get('order_by')
  if order_by == None:
    order_by = "popular"
    new = news(order_by)
  if order_by:
    new = news(order_by)
  else:
    return redirect('/')
  return render_template('index.html', news = new, order_by = order_by)

@app.route('/<id>', methods=['post'])
def comentarios(id):
  r = request.form.get('enviar')
  r = ast.literal_eval(r)
  title = r['title']
  url = r['url']
  points = r['points']
  author = r['author']
  id = r['id']
  comentarios = comments(id)
  return render_template("id.html", comment = comentarios, id = id, title = title, url = url, points = points, author = author)

  
# iniciar servidor
app.run(host="0.0.0.0")