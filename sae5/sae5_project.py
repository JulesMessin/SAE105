"""import sae5_module.py"""

#import pandas as pd
# Lecture du fichier excel et enregistrement des données dans la variable etableau
#table = pd.read_excel("../data/conductivite_amont.xls")


def genere_html(filename, titre_page, body_html):
    fichier = open(filename, 'w')
    fichier.write("".join(body_html))
    fichier.close()
    
def genere_css(filename, titre_page, body_css):
    fichier = open(filename, 'w')
    fichier.write("".join(body_css))
    fichier.close()
    
f="helloworld2"

def main():
    body_html = """ 
                <html>
                <body>
                    <h1> """, f ,"""</h1>
                    <h2> salut c'est moi </h2>
                
                </body>
                </html> 
           """
    genere_html("./index.html", "mon titre", body_html)
    print("La page html a été crée sous le nom de index.html")
    
def stylesheet():
    body_css = """ 
                <html>
                <body>
                    <h1> """, f ,"""</h1>
                    <h2> salut c'est moi </h2>
                
                </body>
                </html> 
           """
    genere_css("./stylesheet.css", "mon titre", body_css)
    print("La page css a été crée sous le nom de stylesheet.css")
   

if __name__ == "__main__":
    print("activation")
    main()
    stylesheet()