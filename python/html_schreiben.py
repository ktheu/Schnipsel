# -*- coding: utf-8 -*-
   
html1 = '''
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style type="text/css">
  body {  color: #555753;
          margin-top: 100px;
          margin-left: 200px;
          font-family: Verdana, Arial, sans-serif;
          font-size: 150%;  }
  </style>
  <title>Unicode</title>
</head>
<body>
<p> '''

html2 = '''  </p>
</body>
</html>
'''

ausgabe = [html1,'Hallo',html2]
with open('output.html','w') as f:
   f.writelines([x+'\n' for x in ausgabe] ) 
       
