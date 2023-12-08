"""import sae5_module.py"""
import xlrd

import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import linspace, array, sin, cos, pi

#Lecture du fichier excel et enregistrement des données dans la variable etableau
book = xlrd.open_workbook("../data/conductivite_amont.xls")


def graphique():
    fig, axes = plt.subplots()  # Creation d'un figure avec un seul axe
    axes.set_xlabel('x') #label de l'axe des abscisses
    axes.set_ylabel('y') #label de l'axe des ordonnées
    axes.set_title('Signal sinusoïdal') #titre du graphique
    #gènère un tableau de 200 points uniformément répartis entre 0 et 2*pi
    x = linspace(0,2*pi,200)
    y = sin(x)
    #dessine la fonction y = f(x) de couleur verte, epaisseur=2
    axes.plot(x, y, color = "green", linewidth= 2, linestyle='-.', label='y = sin(x)')
    y2 = cos(x)
    #avec label écrit en latex
    axes.plot(x, y2, color = "red", lw= 2, linestyle='-', label=r"$y = \cos(x)$")
    #positionne la légende
    axes.legend(loc='best')
    #enregistre une capture de la figure
    fig.savefig("../html/img/graphique.png")

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
                    <nav>
                        <button class="logo"></button>
                        <button class="table"></button>
                        <button class="graphique"></button>
                    </nav>
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
                        <div class="graph">
                            <img class="graphique" src="img/graphique.png" alt="logo">
                        </div>
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
                
                nav {
                  background-color: white;  
                  width: 100%;
                  height: 75px;
                  position: fixed;
                  top: 0px;
                  left: 0px;
                  right: 0px;
                  z-index: 5;
                }
                
                h1 {
                  color : blue;    
                }
                
                div.main {
                  background-color: gray;
                  height: 200%;
                  width: 100%;
                  position: absolute;
                  top: 8%;
                  left: 0px;
                  right: 0px;
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
                
                button.logo {
                 background-image: url("img/universite-poitiers-logo.jpg");
                 width:100px;
                 height:75px;
                  
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