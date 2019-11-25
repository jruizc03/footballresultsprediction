from flask import Flask, request, render_template, json
from neo4j import GraphDatabase
import pandas as pd
from warnings import simplefilter
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import numpy as np

app = Flask(__name__)

simplefilter(action='ignore', category=FutureWarning)
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth= ("neo4j", "pass"))

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/bundesliga", methods=['GET','POST'] )
def bundesliga():
    if request.method == 'GET':
        return render_template('bundesliga.html')
    elif request.method == 'POST':
        cuota_local = request.form.get('cuota_local')
        cuota_empate = request.form.get('cuota_empate')
        cuota_visitante = request.form.get('cuota_visitante')
        equipo_local = request.form.get('equipo_local')
        equipo_visitante = request.form.get('equipo_visitante')

        nombre_equipo_local = getNombreBundesliga(int(equipo_local))
        nombre_equipo_visitante = getNombreBundesliga(int(equipo_visitante))

        with driver.session() as session:
            Bundesliga_df = session.read_transaction(crear_dataframe_encuentros, "Bundesliga")
            session.close()

        df = Bundesliga_df.copy()
        resultado = entrenar_modelo_predecir(Bundesliga_df , df, nombre_equipo_local, nombre_equipo_visitante, cuota_local, cuota_empate, cuota_visitante)
        return render_template('bundesliga.html', cuota_local=cuota_local, cuota_empate=cuota_empate, cuota_visitante=cuota_visitante, resultado=resultado)

def getNombreBundesliga(num):
    switcher={
                1:'Dortmund',
                2:'Leverkusen',
                3:'Bayern Munich',
                4:"M'gladbach",
                5:'Schalke 04',
                6:'Wolfsburg',
                7:'Hoffenheim',
                8:'Hannover',
                9:'Werder Bremen',
                10:'Ein Frankfurt'
             }
    return switcher.get(num,"Invalid team")

def crear_dataframe_encuentros(tx, liga):
    Neo4j_Query = tx.run("MATCH (n:Encuentro { liga: {liga} })--(rf:Resultados_Finales) "
                         "MATCH (n:Encuentro { liga: {liga} })--(rd:Resultados_Descanso) "
                         "MATCH (n:Encuentro { liga: {liga} })--(e:Estadisticas) "
                         "MATCH (n:Encuentro { liga: {liga} })--(c:Cuotas) "
                         "RETURN n.equipo_local AS Equipo_Local, n.equipo_visitante AS Equipo_Visitante,rd.goles_descanso_local AS Goles_Local_Descanso, rd.goles_descanso_visitante AS Goles_Visitante_Descanso, rd.resultado_al_descanso AS Resultado_al_descanso, rf.goles_finales_local AS Goles_Local_Final, rf.goles_finales_visitante AS Goles_Visitante_Final, rf.resultado_final AS Resultado_Final, n.fecha AS Fecha, e.tiros_local AS Tiros_Local, e.tiros_visitante AS Tiros_Visitante, e.tiros_a_puerta_local AS Tiros_A_Puerta_Local, e.tiros_a_puerta_visitante AS Tiros_A_Puerta_Visitante, e.faltas_local AS Faltas_Local, e.faltas_visitante AS Faltas_Visitante, e.corners_local AS Corners_Local, e.corners_visitante AS Corners_Visitante, e.tarjetas_amarillas_local AS Amarillas_Local, e.tarjetas_rojas_local AS Rojas_Local, e.tarjetas_amarillas_visitante AS Amarillas_Visitante, e.tarjetas_rojas_visitante AS Rojas_Visitante, c.Bet365_local AS Bet365Local, c.Bet365_empate AS Bet365Empate, c.Bet365_visitante AS Bet365Visitante, c.bwin_local AS bwinLocal, c.bwin_empate AS bwinEmpate, c.bwin_visitante AS bwinVisitante, c.Interwetten_local AS InterwettenLocal, c.Interwetten_empate AS InterwettenEmpate, c.Interwetten_visitante AS InterwettenVisitante, c.WilliamHill_local AS WilliamHillLocal, c.WilliamHill_empate AS WilliamHillEmpate, c.WilliamHill_visitante AS WilliamHillVisitante ", liga=liga)
    df = pd.DataFrame(Neo4j_Query, columns = ["Equipo_Local", "Equipo_Visitante", "Goles_Descanso_Local", "Goles_Descanso_Visitante", "Resultado_Al_Descanso", "Goles_Final_Local", "Goles_Final_Visitante", "Resultado_Final", "Fecha", "Tiros_Local", "Tiros_Visitante", "Tiros_Puerta_Local", "Tiros_Puerta_Visitante", "Faltas_Local", "Faltas_Visitante", "Corners_Local", "Corners_Visitante", "Amarillas_Local", "Rojas_Local", "Amarillas_Visitante", "Rojas_Visitante", "Bet365_Local", "Bet365_Empate", "Bet365_Visitante", "bwin_Local", "bwin_Empate", "bwin_Visitante", "Interwetten_Local", "Interwetten_Empate", "Interwetten_Visitante", "WilliamHill_Local", "WilliamHill_Empate", "WilliamHill_Visitante"]) 
    pd.set_option('display.max_columns', 33)
    return df.drop_duplicates()

def entrenar_modelo_predecir(df_inicial, df_entrenar, equipo_local, equipo_visitante, cuota_local, cuota_empate, cuota_visitante):
    
    del df_entrenar['bwin_Local']
    del df_entrenar['bwin_Empate']
    del df_entrenar['bwin_Visitante']
    del df_entrenar['Interwetten_Local']
    del df_entrenar['Interwetten_Empate']
    del df_entrenar['Interwetten_Visitante']
    del df_entrenar['WilliamHill_Local']
    del df_entrenar['WilliamHill_Empate']
    del df_entrenar['WilliamHill_Visitante']
    
    del df_entrenar['Fecha']
    del df_entrenar['Equipo_Local']
    del df_entrenar['Equipo_Visitante']
    X = np.array(df_entrenar.drop(['Resultado_Final'],1))
    y = np.array(df_entrenar['Resultado_Final'])
    X.shape
    
    model = linear_model.LogisticRegression()
    model.fit(X,y)
    
    predictions = model.predict(X)
    model.score(X,y)
    validation_size = 0.30
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, y, test_size=validation_size, random_state=seed)
    
    name='Logistic Regression'
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    
    predictions = model.predict(X_validation)
    
    medias_Local  = df_inicial.groupby('Equipo_Local')
    medias_Visitante  = df_inicial.groupby('Equipo_Visitante')
    
    medias_Local = medias_Local.mean()
    medias_Visitante = medias_Visitante.mean()
    
    media_Resultado_Descanso = (medias_Local['Resultado_Al_Descanso'][equipo_local] + medias_Visitante['Resultado_Al_Descanso'][equipo_visitante]) / 2
    
    X_new = pd.DataFrame({'Goles_Descanso_Local':[float(medias_Local['Goles_Descanso_Local'][equipo_local])], 'Goles_Descanso_Visitante':[float(medias_Visitante['Goles_Descanso_Visitante'][equipo_visitante])], "Resultado_Al_Descanso":[media_Resultado_Descanso], "Goles_Final_Local":[float(medias_Local['Goles_Final_Local'][equipo_local])], "Goles_Final_Visitante":[float(medias_Visitante['Goles_Final_Visitante'][equipo_visitante])], "Tiros_Local":[float(medias_Local['Tiros_Local'][equipo_local])], "Tiros_Visitante":[float(medias_Visitante['Tiros_Visitante'][equipo_visitante])], "Tiros_Puerta_Local":[float(medias_Local['Tiros_Puerta_Local'][equipo_local])], "Tiros_Puerta_Visitante":[float(medias_Visitante['Tiros_Puerta_Visitante'][equipo_visitante])], "Faltas_Local":[float(medias_Local['Faltas_Local'][equipo_local])], "Faltas_Visitante":[float(medias_Visitante['Faltas_Visitante'][equipo_visitante])], "Corners_Local":[float(medias_Local['Corners_Local'][equipo_local])], "Corners_Visitante":[float(medias_Visitante['Corners_Visitante'][equipo_visitante])], "Amarillas_Local":[float(medias_Local['Amarillas_Local'][equipo_local])], "Rojas_Local":[float(medias_Local['Rojas_Local'][equipo_local])], "Amarillas_Visitante":[float(medias_Visitante['Amarillas_Visitante'][equipo_visitante])], "Rojas_Visitante":[float(medias_Visitante['Rojas_Visitante'][equipo_visitante])], 'Bet365_Local': [cuota_local], 'Bet365_Empate': [cuota_empate], 'Bet365_Visitante': [cuota_visitante]})
    resultado = model.predict(X_new)
    cadena_resultado = ''
    if(resultado == 0):
        cadena_resultado = 'El ganador es el local'
    elif(resultado == 1):
        cadena_resultado = 'Empate'
    elif(resultado == 2):
        cadena_resultado = 'El ganador es el visitante'
    
    return cadena_resultado

@app.route("/laliga")
def laliga():
    return render_template('laliga.html')

@app.route("/ligueone")
def ligueone():
    return render_template('ligueone.html')

@app.route("/premierleague")
def premierleague():
    return render_template('premierleague.html')

@app.route("/seriea")
def seriea():
    return render_template('seriea.html')

if __name__ == '__main__':
    app.debug = True
    app.run()




