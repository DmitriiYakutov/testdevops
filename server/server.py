from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import psycopg2

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      print('Run server')
      httpd.serve_forever()
  except KeyboardInterrupt:
      print('AHtung')
      httpd.server_close()

def select_from_db():
    conn = psycopg2.connect(dbname='postgresdb', user='postgres',
                            password='postgres', host='127.0.0.1')
    cursor = conn.cursor()
    cursor.execute('select * FROM author LIMIT 10')
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        body = '<body>В базе данных есть записи' + select_from_db() + '</body></html>'
        self.wfile.write(body.encode())

run(handler_class=HttpGetHandler)
