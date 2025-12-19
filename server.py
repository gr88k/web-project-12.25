import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CountriesHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    
    def do_GET(self):
        if self.path == '/countries':
            self.handle_all_countries()

        elif self.path.startswith('/countries/'):
            country_code = self.path.split('/')[-1]
            self.handle_country_detail(country_code)

        else:
            super().do_GET()
    
    def handle_all_countries(self):
        try:
            with open('countries.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
            
        except Exception as e:
            self.send_error(500, str(e))
    
    def handle_country_detail(self, country_code):
        try:
            with open('countries.json', 'r', encoding='utf-8') as f:
                countries = json.load(f)
            
            country = None
            for c in countries:
                if 'cca2' in c and c['cca2'].lower() == country_code.lower():
                    country = c
                    break
            
            if country:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(country, ensure_ascii=False).encode('utf-8'))

            else:
                self.send_response(404)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Country not found"}).encode('utf-8'))
                
        except Exception as e:
            self.send_error(500, str(e))

if __name__ == '__main__':
    print("Server: http://localhost:8000")
    
    server = HTTPServer(('localhost', 8000), CountriesHandler)
    server.serve_forever()