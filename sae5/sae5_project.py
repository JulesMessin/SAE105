"""import sae5_module.py"""

import pandas
#Lecture du fichier excel et enregistrement des données dans la variable etableau
#table = pandas.read_excel("../data/conductivite_amont.xls")


def genere_html(filename, titre_page, body_html):
    fichier = open(filename, 'w')
    fichier.write("".join(body_html))
    fichier.close()
    
def genere_css(filename, titre_page, body_css):
    fichier = open(filename, 'w')
    fichier.write("".join(body_css))
    fichier.close()
    

def main():
    body_html = """ 
                <!DOCTYPE html>
                <html>
                <head>
                    <link rel="stylesheet" href="stylesheet.css">
                </head>
                <body>
                    <header>
                    <img src="img/universite-poitiers-logo.jpg" alt="Italian Trulli">
                    </header>
                    <h1>Voici la page html qui va afficher un tableau et un graphique</h1>
                    <div class="main">
                        <div class="tab">
                            <table>
                            <tr>
                                <td> Titre colonne 1 </td>
                                <td> Titre colonne 2 </td>
                            </tr>
                            <tr>
                                <td>11</td>
                                <td>12</td>
                            </tr>
                            <tr>
                                <td>21</td>
                                <td>22</td>
                            </tr>
                            <tr>
                                <td>31</td>
                                <td>32</td>
                            </tr>
                            </table> 
                        </div>
                        <div class="graph"></div>
                    </div>
                
                </body>
                </html> 
           """
    genere_html("../html/index.html", "mon titre", body_html)
    print("La page html a bien été crée sous le nom de index.html")
    
def stylesheet():
    body_css = """ 
                body {
                  background-color: blue;
                }
                
                header {
                  background-color: white;  
                  height: 100%;
                }
                
                h1 {
                  color : blue;    
                }
                
                div.main {
                  background-color: white;
                  height: 70%;
                  width: 100%;
                }
                div.tab {
                  w
                }
                
                div.graph {
                  w
                }
                table, th, td {
                  border: 1px solid;
                  border-collapse: collapse;
                  
                }
           """
    genere_css("../html/stylesheet.css", "mon titre", body_css)
    print("La page css a bien été crée sous le nom de stylesheet.css")
   

if __name__ == "__main__":
    print("création des fichiers...")
    print("0%...")
    print("25%...")
    print("50%...")
    print("75%...")
    print("100%...")
    main()
    stylesheet()