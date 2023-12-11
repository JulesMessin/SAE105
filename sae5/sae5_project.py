"""import sae5_module.py"""
import openpyxl
import matplotlib.pyplot as plt

#Lecture du fichier excel et enregistrement des données dans les variables value_list et date_list
workbook = openpyxl.load_workbook("../data/conductivite_amont.xlsx", data_only = True)
titres_onglets = workbook.sheetnames
onglet1 = workbook[titres_onglets[0]]
min_row_o1 = onglet1.min_row
max_row_o1 = onglet1.max_row
min_col_o1 = onglet1.min_column
max_col_o1 = onglet1.max_column
for col in onglet1.iter_cols(min_row = min_row_o1, max_row = max_row_o1, min_col = min_col_o1, max_col = max_col_o1, values_only=True):
    if col[0]=='Value':
        value_list=col
    elif col[0]=='Date/Time':
        date_list=col

#conversion de la liste value_list en list, puis on enlève la première valeur de la liste qui est "Valeur"
value_list=list(value_list)
value_list.pop(0)

#conversion de la liste date_list en list, puis on enlève la première valeur de la liste qui est "Date/Time"
date_list=list(date_list)
date_list.pop(0)

#On ferme le fichier excel
workbook.close()

#Création d'une variable date_s_list à partir de la liste date_list, permet d'obtenir le temps en s en focntion du nombre de valeur
date_s_list=[]
for i in range(len(date_list)):
    date_s_list.append(i)
date_s_list=len(date_s_list)/2

# Creation d'un figure
fig = plt.plot(value_list)
plt.xlim(0,date_s_list)
plt.xlabel("Temps en s")
plt.ylabel("Concentration de sel en cm")
plt.title("Concentration en sel au cours du temps")
plt.savefig("../html/img/graphique.png")
plt.show()

def genere_html(filename, titre_page, body_html):
    """

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.
    titre_page : TYPE
        DESCRIPTION.
    body_html : TYPE
        DESCRIPTION.

    Returns
    -------
    Cette fonction va permettre de générer le fichier html.

    """
    fichier = open(filename, 'w')
    fichier.write("".join(body_html))
    fichier.close()
    
def genere_css(filename, titre_page, body_css):
    """

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.
    titre_page : TYPE
        DESCRIPTION.
    body_css : TYPE
        DESCRIPTION.

    Returns
    -------
    Cette fonction va permettre de générer le fichier css.

    """
    fichier = open(filename, 'w')
    fichier.write("".join(body_css))
    fichier.close()
    

def main():
    """

    Returns
    -------
    Création de la structure de la page html.

    """
    body_html = """ 
                <!DOCTYPE html>
                <html>
                <head>
                    <link rel="stylesheet" href="stylesheet.css">
                </head>
                <body>
                    <nav>
                        <a href="https://www.univ-poitiers.fr/"><img src="img/universite-poitiers-logo.jpg" alt="logo"></a>
                        <a href="">Graphique</a>
                        <a href="">Graphique</a>
                    </nav>
                    
                    <h1>Voici la page html qui va afficher un tableau et un graphique</h1>
                    
                    <div class="description" >
                        <p>blabazbdsauhbduahdhzuiahdiuahduiahdaudhaidh
                        blabazbdsauhbduahdhzuiahdiuahduiahdaudhaidh
                        blabazbdsauhbduahdhzuiahdiuahduiahdaudhaidh
                        blabazbdsauhbduahdhzuiahdiuahduiahdaudhaidh
                        blabazbdsauhbduahdhzuiahdiuahduiahdaudhaidh
                        blabazbdsauhbduahdhzuiahdiuahduiahdaudhaidh</p>
                    </div>
                    
                    <div class="tab">
                        <p></p>
                        <table>
                        <tr>
                            <td> ,colonne_1, </td>
                            <td> ,colonne_2, </td>
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
                        <img src="img/graphique.png" alt="logo">
                    </div>
                    
                
                </body>
                </html> 
           """
    genere_html("../html/index.html", "mon titre", body_html)
    print("La page html a bien été crée sous le nom de index.html")
    
def stylesheet():
    """

    Returns
    -------
    Création de la structure de la page css.

    """
    body_css = """ 
                body {
                  background-color: blue;
                }
                
                nav {
                  background-color: white;  
                  width: 91%;
                  margin-left: 4%;
                  margin-right: 5%;
                  height: 75px;
                  position: fixed;
                  margin-top: 10px;
                  z-index: 5;
                  display: inline;
                  border-radius: 10px;
                }
                
                nav a  {
                        
                }
                
                h1 {
                  color : blue;    
                }
                
                div.description {
                  background-image: url("img/wallpaper_description.jpeg");
                  background-size: cover;
                  background-repeat: no-repeat;
                  height: 100%;
                  width: 100%;
                  position: absolute;
                  top: 0px;
                  left: 0px;
                  right: 0px;
                  text-align: center;
                }
                
                div.description p {
                  margin-top: 23%;  
                  color: gray;
                  font-weight: bolder;
                  font-size: 150%;
                }

                div.tab {
                  background-color: #686868;
                  height: 100%;
                  width: 100%;
                  position: absolute;
                  top: 100%;
                  left: 0px;
                  right: 0px;
                  align-items: center;
            
                }
                
                div.graph {
                  background-color: #E9E9E9;
                  height: 1000px;
                  width: 100%;
                  position: absolute;
                  top: 200%;
                  left: 0px;
                  right: 0px;
                  text-align: center;
                  justify-content: center;
                  
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
                
                
  
                nav a:hover {
                  background-color: red;
                  color:white;
                }
                
                nav a img{
                  position: absolute;
                  width: 100px;
                  height: 70px; 
                  top: 50%;
                  left: 50%;
                  transform: translate(-50%, -50%);
                }
      
                div.graph img {
                  position: absolute;
                  top: 50%;
                  left: 50%;
                  transform: translate(-50%, -50%);
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
    