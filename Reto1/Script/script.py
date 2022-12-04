import gspread
import pandas as pd

sa = gspread.service_account('service_account.json') #Clave generada por el api
sh = sa.open("DataTEST") # Nombre del sheel
wks = sh.worksheet("Reto1") #Nombre de la hoja
df = pd.DataFrame(wks.get_all_records()) #Se recuperan los datos de la hoja actual

#Guardar la informacion en un cvs para manejo de datos 
filename = sh.title + '.csv'
df.to_csv(filename, index=False)
df = pd.read_csv(filename)
#Uso de dummies para modificar la data y gusdarlo en un objeto de nombre rs
Country=pd.get_dummies(df['Country'])
Theme=pd.get_dummies(df['Theme'])
rs=pd.concat([df['Author'], df['Sentiment'],Country,Theme], axis=1)
#Crecion de una hoja para mostrar los resultados en el mismo documento
worksheet = sh.get_worksheet(1)
sh.del_worksheet(worksheet)
worksheet = sh.add_worksheet(title="Resultado", rows=len(rs), cols=len(rs.columns))
wh1 = sh.worksheet("Resultado")
wh1.update([rs.columns.values.tolist()] + rs.values.tolist())


# Link : https://docs.google.com/spreadsheets/d/10ETaeGGKUZEoDU9tCh36O853VTsFkGBCdLFMTR2PaKs/edit?usp=sharing