import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


header=st.container()
dataprocess=st.container()
datavisual=st.container()
datainfo=st.container()


with header:
    st.set_page_config(layout='wide')
    st.title('**INTERACTIVE DASHBOARD OF HEART DISEASE**')
    st.text('To analyze clinical and demographic factors in the heart disease dataset to identify trends, patterns, and potential risk factors associated with heart disease.')

with dataprocess:
    file=st.file_uploader('UPLOAD DATASET HERE',['xlx','xlsx','csv','txt','json'])
    
      def func_load(file):
          data = None
          try:
              if file:
                  if file.name.endswith('.csv'):
                      data = pd.read_csv(file)
                  elif file.name.endswith(('.xls', '.xlsx')):
                      data = pd.read_excel(file)
                  elif file.name.endswith('.json'):
                      data = pd.read_json(file)
                  elif file.name.endswith('.txt'):
                      data = pd.read_csv(file, delimiter='\t')
                  else:
                      st.warning("⚠ Unsupported file format")
              else:
            # Attempt to load local fallback
                  fallback_path = "C:/Users/sa539/Downloads/heart.csv"
                  try:
                      data = pd.read_csv(fallback_path)
                  except FileNotFoundError:
                      pass  # Silent if local file is also missing
          except Exception as e:
              st.warning(f"⚠ Something went wrong while loading the file: {e}")
          return data
    
    
    df=func_load(file)
    
    #data cleanig and making it more redable


    df=df.dropna(subset=['age'])
    df['sex'] = df['sex'].replace({1: 'M', 0: 'F'})
    df['cp'] = df['cp'].map({
    0: 'Typical Angina',
    1: 'Atypical Angina',
    2: 'Non-anginal Pain',
    3: 'Asymptomatic'})
    df['target'] = df['target'].map({1: 'Disease', 0: 'No Disease'})
    df1=df


with st.sidebar:
    if st.toggle('**About**'):
        st.write("""
             1. Analyzes heart disease dataset using patient health records
             2. Focuses on trends and patterns using visualizations
             3. Aims to identify key risk factors (age, cholesterol, etc.)
             4. Purely exploratory (no machine learning)
             5. Helps understand factors linked to heart disease""")
    col_des=st.checkbox('SHOW COLUMN DESCRIPTION')
    filter_data=st.checkbox('**SHOW FILTERS**')
    if filter_data :

        sex=st.multiselect('Select Gender',df['sex'].unique(),df['sex'].unique()[1])
        df=df[df['sex'].isin(sex)]

        cp=st.multiselect('Select CP',df['cp'].unique(),df['cp'].unique()[0])
        df=df[df['cp'].isin(cp)]

        age_min, age_max = int(df['age'].min()), int(df['age'].max())
        age_range = st.sidebar.slider("Select Age Range", min_value=age_min, max_value=age_max, value=(age_min, age_max))
        df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
        
        chol_min, chol_max = int(df['chol'].min()), int(df['chol'].max())
        chol_range = st.sidebar.slider("Select Chol Range", min_value=chol_min, max_value=chol_max, value=(chol_min, chol_max))
        df = df[(df['chol'] >= chol_range[0]) & (df['chol'] <= chol_range[1])]

        target_filter=st.radio('Heart Disease',options=['All','Disease','No Disease'])
        if target_filter=='Disease':
            df=df[df['target']=='Disease']
        elif target_filter=='No Disease':
            df=df[df['target']=='No Disease']
    data_descrip=st.sidebar.button('DATA DESCRIPTION')
    uni_num_plot=st.selectbox('Numerical Column For Histogram or KDE',['age','chol','trestbps','thalach'])
    uni_cat_plot=st.selectbox('Categorical Column For Count Plot',['sex','cp','restecg','exang'])
    uni_num_box=st.selectbox('Check Outlier in :',['trestbps','thalach','chol','age'])

    #mean showing on siedbar
    mean_num_data=st.button('Show Average of Numeric Column')
    mean_df=df.groupby('target')[['thalach','chol','trestbps']].mean().reset_index()

    if mean_num_data:
        mean_df=mean_df.melt(id_vars='target',var_name='Feature',value_name='Average')
        st.dataframe(mean_df)
    else:
        pass
    toggle_age_chol=st.toggle('Toggal (age-chol)',['age','chol'])
    switch_age_thal=st.toggle('Toggal (age-thalach)',['age','thalach'])
    st.write('Age,chol,thalach over target')
    show_3D_plot=st.button('Show 3D')


with datavisual:
    see_data=st.checkbox('SHOW DATASET')
    col1,col2=st.columns([2,4])
    with col1:
        if col_des:
            st.markdown("### 🧾 Dataset Column Descriptions")
            st.markdown("""
| Column     | Description                                |
| ---------- | ------------------------------------------ |
| `age`      | Age of the patient                         |
| `sex`      | 1 = male, 0 = female                       |
| `cp`       | Chest pain type (0–3)                      |
| `trestbps` | Resting blood pressure                     |
| `chol`     | Serum cholesterol                          |
| `fbs`      | Fasting blood sugar > 120 mg/dl (1 = true) |
| `restecg`  | Resting electrocardiographic results       |
| `thalach`  | Maximum heart rate achieved                |
| `exang`    | Exercise-induced angina                    |
| `oldpeak`  | ST depression induced by exercise          |
| `slope`    | Slope of the peak exercise ST segment      |
| `ca`       | Number of major vessels (0–3) colored      |
| `thal`     | Thalassemia type                           |
| `target`   | 1 = heart disease present, 0 = not present |""")
  
    
    with col2:
        if not(filter_data):
            if see_data:
                st.subheader('Raw Data Preview')
                st.dataframe(df1)
                if data_descrip:
                    st.write(df1.describe())
                    st.write(f'NO. OF PEOPLE: {df1.shape[0]}')
                else:
                    pass 
            else:
                pass
        else:
            if see_data:
                st.subheader('Filtered Data Preview')
                st.dataframe(df)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("Download Filtered CSV", csv, "filtered_heart_data.csv", "text/csv")
                if data_descrip:
                    st.write(df.describe())
                    st.write(f'NO. OF PEOPLE: {df.shape[0]}')
                else:
                    pass
    #univerate data analysis
    col3,col4=st.columns(2)
    with col3:
        
        fig1=px.bar(df.groupby([uni_cat_plot,'target']).size().reset_index(name='count'),x=uni_cat_plot,y='count',barmode='group',color='target',title=f'Heart Disease Count by {uni_cat_plot}',text='count')
        st.plotly_chart(fig1,use_max_width=True)

    with col4:

        fig1=px.histogram(df,x=uni_num_plot,nbins=10,color='target',title=f'Heart Disease Count by {uni_num_plot}')
        st.plotly_chart(fig1,use_max_width=True)

    fig1=px.box(df,y=uni_num_box,points='all',color='target',title=f'Heart Disease Distribution by {uni_num_box}')
    st.plotly_chart(fig1,use_max_width=True)


    col5,col6=st.columns(2)
    with col5:
        if toggle_age_chol:
            fig1=px.violin(df,y='age',x='target',title='Age Distribution Over Target')
            st.plotly_chart(fig1,use_max_width=True)
        else:
            fig1=px.violin(df,y='chol',x='target',title=f'{toggle_age_chol} Distribution Over Target')
            st.plotly_chart(fig1,use_max_width=True)
        
    with col6:
        fig1=px.bar(df,y=['thalach','chol','trestbps'],x='target',color_discrete_sequence=['pink','grey','purple'],title='Distribution Over Thalach,Chol and Trestbps')
        st.plotly_chart(fig1,use_max_width=True)
    
    st.subheader('Heart Disease Discreption over thalach(Max heart rate) and age_group')
        
    col7,col8=st.columns(2)
    df['age_group']=pd.cut(df['age'],bins=[0,10,20,30,40,50,60,70,80,90],labels=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90'])
    with col7:
        @st.cache_resource
        def create_swarmplot(data):
            fig1, ax = plt.subplots(figsize=(12,8))
            ax=sns.swarmplot(df,x='age_group',y='thalach',hue='target')
            ax.set_title(f'Swarmplot of {switch_age_thal} by Heart Disease')
            plt.legend(bbox_to_anchor=(1.05,1),loc='lower left')
            return fig1
        fig1=create_swarmplot(df)
        st.pyplot(fig1)
    
    with col8:
        @st.cache_resource
        def create_violinplot(data):
            fig, ax = plt.subplots(figsize=(12,8))
            ax=sns.violinplot(df,x='age_group',y='thalach',hue='target')
            ax.set_title(f'Violin Plot of Max Heart Rate by Heart Disease')
            plt.legend(bbox_to_anchor=(1.05,1),loc='lower left')
            return fig
        fig=create_violinplot(df)
        st.pyplot(fig)

    #multivarite analysis
    col9,col10=st.columns([220,580])

    with col9:
        corr = df[['thalach', 'age', 'exang']].corr()
        fig = px.imshow(corr, text_auto=".2f", color_continuous_scale='RdBu',zmin=-1, zmax=1, title="Thalach, Age, and Exang Correlation")
        st.plotly_chart(fig, use_container_width=True)
    
    with col10:
        st.markdown("&nbsp;" * 4, unsafe_allow_html=True)
        st.write("**Pairplot of target and age,chol,thalach Variables by Sex**")
        @st.cache_resource
        def create_pairplot(data):
            pairplot=sns.pairplot(data,hue='sex',hue_order=['F','M'],palette='Blues',x_vars=['age','chol','thalach'],y_vars=['target'],markers=['*','^'])
            pairplot.fig.suptitle("Pairplot", y=1.1, fontsize=16)
            return pairplot
        fig=create_pairplot(df)
        st.pyplot(fig)
    
    st.subheader('Cp(Cardiac Pain) Distribution over target(Disease/Non Diseaese)')
    @st.cache_resource
    def create_catplot(data):
        fig2 = sns.catplot(
        data=data,
        x='cp', hue='target', col='sex',
        kind='count', palette='Oranges',
        height=5, aspect=1.25)
        return fig2

    fig = create_catplot(df)
    st.pyplot(fig)

    fig4=px.scatter(df,x='age',y='thalach',color='target',title='Age-Thalach over target')
    st.plotly_chart(fig4,use_container_width=True)

    @st.cache_resource
    def load_3d_scatter(data):
            fig5=px.scatter_3d(df,x='age_group',y='chol',z='thalach',color='sex',hover_data='target',category_orders={'age_group':['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90']},title='Age-group,Chol,Thalach 3D Interprecation')
            st.plotly_chart(fig5, use_container_width=True)
    if show_3D_plot:
        load_3d_scatter(df)
        









    


        




