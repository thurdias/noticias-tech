import requests 
from bs4 import BeautifulSoup

def news(order_by):
  if order_by == "popular" or order_by == "":
    pop_news = []
    r = requests.get("https://hn.algolia.com/api/v1/search?tags=story")
    r = r.json()
    n = len(r['hits'])
    for noticias in r:
      for length in range(n):
        noticiap = {
          'title': r['hits'][length]['title'],
          'url': r['hits'][length]['url'],
          'author': r['hits'][length]['author'],
          'points': r['hits'][length]['points'],
          'num_comments': r['hits'][length]['points'],
          'id': r['hits'][length]['objectID']
        }
        pop_news.append(noticiap)   
    return pop_news 
  else:
    new_news = []
    r = requests.get("https://hn.algolia.com/api/v1/search_by_date?tags=story")
    r = r.json()
    n = len(r['hits'])
    for noticias in r:
      for length in range(n):
        notician = {
          'title': r['hits'][length]['title'],
          'url': r['hits'][length]['url'],
          'author': r['hits'][length]['author'],
          'points': r['hits'][length]['points'],
          'num_comments': r['hits'][length]['points'],
          'id': r['hits'][length]['objectID']    
        }
        new_news.append(notician) 
    return new_news 

def comments(id):
  r = requests.get(f"https://hn.algolia.com/api/v1/items/{id}")
  r = r.json()
  a = len(r['children'])
  comentarios = []
  for length in range(a):
    if r['children'][length]['author'] == None:
      comentario = {
        "author": "[deleted]"
      }
    else:
      comentario = BeautifulSoup(r['children'][length]['text'], features='html.parser')   
      comentario = {
        "author":r['children'][length]['author'],
        "comentario": comentario,
      }
    comentarios.append(comentario)
  return comentarios