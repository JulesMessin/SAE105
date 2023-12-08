"""import sae5_module.py"""
import xlrd

import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import linspace, array, sin, cos, pi

#Lecture du fichier excel et enregistrement des données dans la variable etableau

def tableau():
    tab = xlrd.open_workbook("../data/conductivite_amont.xls")
    
    print("Nombre de feuilles: "+str(tab.nsheets))
    print("Noms des feuilles: "+str(tab.sheet_names()))
    
    feuille_1 = tab.sheet_by_index(0)
    feuille_1 = tab.sheet_by_name("Fonction 1")
    
    print("Format de la feuille 1:")
    print("Nom: "+str(feuille_1.name))
    print("Nombre de lignes: "+str(feuille_1.nrows))
    print("Nombre de colonnes: "+str(feuille_1.ncols))
    
    cols = feuille_1.ncols
    rows = feuille_1.nrows
    
    X = []
    Y= []
    
    for r in range(1, rows):
        X += [feuille_1.cell_value(rowx=r, colx=0)]
        Y += [feuille_1.cell_value(rowx=r, colx=1)]
    
    plt.plot(X, Y)
    plt.show()
        
    
    

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
                        <div class="logo"><a href="https://www.univ-poitiers.fr/"><img class="logo" src="img/universite-poitiers-logo.jpg" alt="logo"></a></div>
                        <div class="table"></div>
                        <div class="graphique"></div>
                    </nav>
                    <h1>Voici la page html qui va afficher un tableau et un graphique</h1>
                    <div class="description" ></div>
                    <div class="tab">
                        <table>
                        <tr>
                            <td> """,colonne_1,""" </td>
                            <td> """,colonne_2,""" </td>
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
                
                div.description {
                  background-color: gray;
                  height: 500px;
                  width: 100%;
                  position: absolute;
                  top: 75px;
                  left: 0px;
                  right: 0px;
                }
                
                div.tab {
                  background-color: #a3a3a3;
                  height: 1000px;
                  width: 100%;
                  position: absolute;
                  top: 575px;
                  left: 0px;
                  right: 0px;
            
                }
                
                div.graph {
                  background-color: #7a7878;
                  height: 1000px;
                  width: 100%;
                  position: absolute;
                  top: 1575px;
                  left: 0px;
                  right: 0px;
                  
                }
                
                table, th, td {
                  border: 1px solid;
                  border-collapse: collapse;
                }
                
                table {
                  position: relative;  
                  right:40%
                  top: 100px;
                  
                }
                div.logo {
                 width: 100px;
                 height: 75px;
                }
                
                img.logo {
                  width: 100%;  
                  height:100%;  
                    
                }
                
                img.graphique {
                  position: absolute;
                  display: block;
                  margin: auto;
                  width: 700px;  
                  height: 500px;  
                    
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