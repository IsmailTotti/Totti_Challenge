import requests

def test_hello_api():
    url = "https://fspc34yew9.execute-api.us-east-1.amazonaws.com/dev/hello"
    response = requests.get(url)
    
    assert response.status_code == 200
    expected = '''
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>
'''.strip()
    assert response.text.strip() == expected
#test_hello_api()