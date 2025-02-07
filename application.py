"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy seaborn streamlit matplotlib.pyplot plotly.express
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

# conda create -n projet python pandas numpy matplotlib jupyterlab kagglehub seaborn streamlit plotly
# conda activate projet
# h:
# cd H:\BUT3\SAE\sae_601
# streamlit run application.py


### 1. Importation des librairies et chargement des données
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Chargement des données
df = pd.read_csv("ds_salaries.csv") 

titres_onglets = ['Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6', 'Question 7', 'Question 8', 'Question 9','Question 10']
onglet1, onglet2, onglet3, onglet4, onglet5, onglet6, onglet7, onglet8, onglet9 = st.tabs(titres_onglets)
with onglet1:
    st.header('Question 2')
    ### 2. Exploration visuelle des données
    #votre code     
    st.title("📊 Visualisation des Salaires en Data Science")
    st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")
    if st.checkbox("Afficher un aperçu des données"):
        st.write(df)
    #Statistique générales avec describe pandas 
    #votre code
    st.subheader("📌 Statistiques générales")
    st.write(df.describe())
 
with onglet2:
    st.header('Question 3')
    ### 3. Distribution des salaires en France par rôle et niveau d'expérience, uilisant px.box et st.plotly_chart
    #votre code
    data_france = df[df['company_location']=='FR']
    fig3 = px.box(
        data_france,
        x='job_title', 
        y='salary_in_usd', 
        color='experience_level',
        title='Distribution des salaires en France par métier et niveau d\'expérience',
        labels={'job_title': 'Métier', 'salary_in_usd': 'Salaire', 'experience_level': 'Niveau d\'expérience'},
        height=600
    )
    st.subheader("📈 Distribution des salaires en France")
    st.plotly_chart(fig3)
    st.markdown("Ce graphique montre la répartition des salaires en France pour divers métiers technologiques, selon trois niveaux d'expérience : débutant, intermédiaire et expert. On observe que les experts (en rouge) ont les salaires les plus élevés, alors qu'ils soient concentrés sur quelques métiers comme 'Data Scientist' ou 'Machine Learning Research Engineer'. Les débutants (en bleu foncé) ont des salaires plus homogènes, avec des métiers tels que 'Data DevOps Engineer'. Les intermédiaires (en bleu clair) présentent une plus grande variabilité, particulièrement pour les postes de 'Data Scientist', montrant des écarts significatifs entre entreprises et compétences.")

with onglet3:
    st.header('Question 4')
    ### 4. Analyse des tendances de salaires :
    #### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox
    st.subheader("📊 Analyse des tendances de salaires")
    categories = ['experience_level', 'employment_type', 'job_title', 'company_location']
    selected_category = st.selectbox("catégorie pour analyser le salaire moyen :",categories)
    average_salary = df.groupby(selected_category)['salary_in_usd'].mean().reset_index()
    average_salary = average_salary.rename(columns={'salary_in_usd': 'average_salary'})
    fig4 = px.bar(
        average_salary,
        x=selected_category,
        y='average_salary',
        title=f"Salaire moyen par {selected_category}",
        labels={selected_category: "Catégorie", 'average_salary': "Salaire moyen"},
        height=600
    )   
    st.plotly_chart(fig4)
    st.markdown("Filtre par `experience_level` : Ce graphique montre que les salaires moyens augmentent significativement avec l'expérience. Les experts ont les salaires les plus élevés, dépassant largement 200k, tandis que les débutants et intermédiaires se situent autour de 100k.")
    st.markdown("Filtre par `employment_type` : Ce graphique montre que les employés à temps plein ont les salaires les plus élevés, dépassant les 140k en moyenne, suivis par les contrats permanents, qui se situent autour de 100k. Les contrats freelance et à temps partiel affichent des salaires nettement plus bas, ce qui reflète probablement des rémunérations moins stables et moins compétitives.")
    st.markdown("Filtre par `job_title` : Ce graphique montre la forte variabilité des salaires selon les métiers. Les postes liés au machine learning, à la data science et aux rôles de direction ont les salaires les plus élevés, dépassant parfois les 300k. En revanche, des métiers plus techniques ou spécifiques, comme les techniciens ou analystes, ont des salaires moyens plus modestes.")
    st.markdown("Filtre par `company_location` : Ce graphique montre des disparités géographiques importantes dans les salaires moyens. Certaines régions, comme les États-Unis, offrent des salaires bien plus élevés, dépassant 250k, tandis que d'autres pays montrent des moyennes beaucoup plus basses.")

with onglet4:
    st.header('Question 5')
    ### 5. Corrélation entre variables
    # Sélectionner uniquement les colonnes numériques pour la corrélation
    #votre code 
    numeric_columns = df.select_dtypes(include=['float64', 'int64'])
    # Calcul de la matrice de corrélation
    #votre code
    correlation_matrix = numeric_columns.corr()
    # Affichage du heatmap avec sns.heatmap
    #votre code
    st.subheader("📊 Corrélations entre variables numériques")
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="PiYG", cbar=True)
    st.pyplot(plt)
    st.markdown("""
    Ce graphique montre les corrélations entre différentes variables numériques. 
    - La variable `work_year` a une corrélation positive avec `salary_in_usd` (0.23), mais une corrélation négative avec `remote_ratio` (-0.24) et `salary` (-0.095). Cela signifie que plus l'année de travail augmente, plus les salaires en dollars augmentent, mais moins le travail à distance est pratiqué.
    - La variable `salary` a une faible corrélation positive avec `remote_ratio` (0.029), mais presque aucune corrélation avec `salary_in_usd` (-0.024). Cela indique que le salaire local n'a pas beaucoup d'impact sur le ratio de télétravail ou les salaires en dollars.
    - La variable `salary_in_usd` a une faible corrélation négative avec `remote_ratio` (-0.064). Cela montre que les salaires en dollars ne dépendent pas beaucoup du travail à distance.
    - La variable `remote_ratio` a une faible corrélation positive avec `salary` (0.029) et une corrélation négative avec `work_year` (-0.24). Cela montre que le travail à distance est légèrement plus courant pour des salaires locaux élevés, mais tend à diminuer avec les années de travail.
    """)
    


with onglet5:
    st.header('Question 6')
    ### 6. Analyse interactive des variations de salaire
    # Une évolution des salaires pour les 10 postes les plus courants
    # count of job titles pour selectionner les postes
    # calcule du salaire moyen par an
    #utilisez px.line
    #votre code 
    #10 postes les plus courants
    top_jobs = df['job_title'].value_counts().head(10).index
    #filtre
    filtered_data = df[df['job_title'].isin(top_jobs)]
    #salaire moyen par année et poste
    salary_trends = (
        filtered_data.groupby(['work_year', 'job_title'])['salary_in_usd']
        .mean()
        .reset_index()
        .rename(columns={'salary_in_usd': 'average_salary'})
    )
    fig6 = px.line(
        salary_trends,
        x='work_year',
        y='average_salary',
        color='job_title',
        title="Evolution des salaires moyens pour les 10 postes les plus courants",
        labels={'work_year': 'Année', 'average_salary': 'Salaire moyen', 'job_title': 'Poste'},
        markers=True,
        height=600
    )
    st.subheader("📈 Analyse interactive des variations de salaire")
    st.plotly_chart(fig6)
    st.markdown(   
    """
Ce graphique montre l'évolution des salaires moyens pour les 10 postes les plus courants entre 2020 et 2023.

- Le poste de `Data Scientist` affiche une progression constante, atteignant l'un des salaires les plus élevés en 2023, au-delà de 200k.

- Le poste de `Machine Learning Engineer` montre également une augmentation régulière, se situant parmi les postes les mieux rémunérés.

- Le poste de `Data Science Manager` connaît une forte augmentation entre 2021 et 2022, dépassant également 200k en 2023.

- Les postes de `Data Engineer`, `Data Analyst` et `Research Scientist` présentent des progressions plus modestes mais régulières, avec des salaires moyens autour de 100k à 150k en 2023.

- Le poste de `Applied Scientist` affiche une augmentation rapide après une chute en 2021, atteignant un niveau compétitif en 2023.

- Le poste de `Analytics Engineer` connaît une progression plus modérée, restant dans la moyenne basse des salaires observés.

- Les postes de `Data Architect` et `Research Engineer` montrent des variations notables, mais globalement une tendance à la hausse.


""")


with onglet6:
    st.header('Question 7')
    ### 7. Salaire médian par expérience et taille d'entreprise
    # utilisez median(), px.bar
    #votre code 
    #salaire médian par niv d'exp et taille entreprise
    median_salary = (
        df.groupby(['experience_level', 'company_size'])['salary_in_usd']
        .median()
        .reset_index()
        .rename(columns={'salary_in_usd': 'median_salary'})
    )
    fig7 = px.bar(
        median_salary,
        x='experience_level',
        y='median_salary',
        color='company_size',
        barmode='group',
        title="Salaire médian par niveau d'expérience et taille d'entreprise",
        labels={
            'experience_level': 'Niveau d\'expérience',
            'median_salary': 'Salaire médian',
            'company_size': 'Taille d\'entreprise'
        },
        height=600
    )
    st.subheader("📊 Salaire médian par expérience et taille d'entreprise")
    st.plotly_chart(fig7)
    st.markdown(  
    """
Ce graphique montre le salaire médian en fonction du niveau d'expérience et de la taille d'entreprise.

- Pour le niveau `EN`, les salaires médians sont similaires dans les grandes, moyennes, et petites entreprises, autour de 50k.

- Pour le niveau `EX`, les grandes entreprises et les moyennes entreprises offrent des salaires médians proches de 200k, tandis que les petites entreprises restent légèrement en retrait.

- Pour le niveau `MI`, les grandes entreprises et les moyennes entreprises affichent des salaires médians d’environ 100k, tandis que les petites entreprises sont nettement plus basses.

- Pour le niveau `SE`, les grandes entreprises ont des salaires légèrement plus élevés que les moyennes, et les petites entreprises sont en retrait, bien que la différence soit moins marquée qu'aux autres niveaux.


""")

with onglet7:
    st.header('Question 8')
    ### 8. Ajout de filtres dynamiques
    #Filtrer les données par salaire utilisant st.slider pour selectionner les plages 
    #votre code 
    st.subheader("📊 Filtre par salaire")
    #slider pour sélectionner une plage de salaires
    min_salary = int(df['salary_in_usd'].min())
    max_salary = int(df['salary_in_usd'].max())
    selected_range = st.slider(
        "Sélectionnez une plage de salaires",
        min_value=min_salary,
        max_value=max_salary,
        value=(min_salary, max_salary)
    )
    #filtre
    filtered_data = df[(df['salary_in_usd'] >= selected_range[0]) & (df['salary_in_usd'] <= selected_range[1])]
    #afficher
    st.write(f"Nb d'entrées après filtre : {len(filtered_data)}")
    st.dataframe(filtered_data)
    st.markdown(
"""
Ce graphique montre un filtre appliqué sur les salaires, avec une plage sélectionnée entre 5,132 et 450,000.

- La colonne `work_year` montre que toutes les données sont pour l'année 2023.

- La colonne `experience_level` montre que les données filtrées couvrent différents niveaux d'expérience, `SE`  et `MI`.

- La colonne `employment_type` montre principalement des contrats à temps plein et quelques contrats temporaires.

- La colonne `job_title` montre des postes variés, comme `Principal Data Scientist`, `ML Engineer`, `Data Scientist`, et `Applied Scientist`.

- La colonne `salary` varie de 25,500 à 222,200 avec des monnaies spécifiées dans la colonne `salary_currency`.

""")


with onglet8:
    st.header('Question 9')
    ### 9.  Impact du télétravail sur le salaire selon le pays
    #calcul salaire moyen par télétravail et pays
    remote_salary = (
        df.groupby(['remote_ratio', 'company_location'])['salary_in_usd']
        .mean()
        .reset_index()
        .rename(columns={'salary_in_usd': 'average_salary'})
    )
    fig9 = px.bar(
        remote_salary,
        x='company_location',
        y='average_salary',
        color='remote_ratio',
        barmode='group',
        title="Impact du télétravail sur le salaire par pays",
        labels={
            'company_location': 'Pays',
            'average_salary': 'Salaire moyen',
            'remote_ratio': 'Ratio de télétravail'
        },
        height=600
    )
    st.subheader("📊 Impact du télétravail sur le salaire selon le pays")
    st.plotly_chart(fig9)
    st.markdown(
"""
Ce graphique montre une relation entre le télétravail et les salaires moyens selon les pays, avec une forte variabilité. 
Certains pays affichent des salaires nettement plus élevés, dépassant parfois 500k, tandis que d’autres restent bien en dessous. 
La coloration des barres indique que dans certains pays, un fort ratio de télétravail est associé à des salaires élevés donc des emplois compatibles avec le télétravail, 
comme ceux du secteur technologique, sont généralement mieux rémunérés. Cependant, les pays avec peu de télétravail présentent souvent des salaires plus bas, 
ce qui pourrait refléter une prédominance d’emplois moins adaptés au télétravail. On observe également une forte dispersion des salaires au sein de certains pays, 
ce qui montre l’importance des écarts intra-pays.
""")

  
with onglet9:
    st.header('Question 10')
    ### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
    #votre code 
    st.subheader("🔍 Filtre des données")
    #selects
    experience_levels = df['experience_level'].unique().tolist()
    company_sizes = df['company_size'].unique().tolist()

    selected_experience = st.multiselect(
        "Sélectionnez le niveau d'expérience",
        options=experience_levels,
        default=experience_levels  
    )

    selected_company_size = st.multiselect(
        "Sélectionnez la taille d'entreprise",
        options=company_sizes,
        default=company_sizes 
    )
    #filtre
    filtered_data = df[
        (df['experience_level'].isin(selected_experience)) &
        (df['company_size'].isin(selected_company_size))
    ]
    #afficher
    st.write(f"Nb d'entrées après filtrage : {len(filtered_data)}")
    st.dataframe(filtered_data)
    st.markdown(
"""
Ce tableau présente les résultats d'un filtrage des données basé sur le niveau d'expérience et la taille de l'entreprise. 
Il affiche diverses informations telles que l’année de travail, le niveau d'expérience, le type d'emploi, l'intitulé du poste, le salaire et la devise utilisée. On y observe plusieurs postes liés à la science des données, 
comme Principal Data Scientist, ML Engineer, Data Scientist et Applied Scientist, avec des salaires variant considérablement en fonction du poste et de la localisation, exprimés en EUR ou USD. 
Par exemple, un Data Scientist peut percevoir des salaires allant de 120 000 à 219 000 USD, tandis qu’un ML Engineer affiche des rémunérations plus basses. 
Ce filtrage permet d'extraire des tendances salariales en fonction du niveau d'expérience et de la taille de l'entreprise.
""")




























