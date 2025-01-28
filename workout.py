import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from geopy.geocoders import Nominatim

st.set_page_config(
    page_title="Workout",           # Заглавие на страницата
    page_icon="🏋️‍♂️",               # Може да бъде емоджи или път към изображение (favicon)
    layout="wide"                 # Оформление: "centered" (по подразбиране) или "wide"
)
st.title("Анализ на тренировки")


st.markdown("""
<style>
.stButton button {
    background-color: #4CAF50; /* Зелен цвят за основния бутон */
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 2px 2px;
    cursor: pointer;
    border: none;
    border-radius: 8px;
    width: 200px
}

.stButton button:hover {
  background-color: #3e8e41; /* По-тъмно зелено при посочване */
  color: black;
}

.stButton button:active {
  background-color: #33691e; /* Най-тъмно зелено при кликване */
  box-shadow: 0 5px #666;
  transform: translateY(4px);
  color: yellow;
}
.sidebar {
  background-color: #cfcc82; /* Светло сив цвят */
}

            
[data-testid="stSidebar"] {
    background-color: #ace3e6;
    color: #333;
    font-family: Arial, sans-serif;
    font-size: 16px;
}
[data-testid="stAppViewContainer"] {
    background-color: #daf3f5;
}
</style>
""", unsafe_allow_html=True)



# # Функция за зареждане на CSS от файл
# def load_css(file_path):
#     with open(file_path) as f:
#         return f.read()

# # Зареждане на CSS
# css_content = load_css("style/style.css")
# st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)


# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# local_css("style/style.css")





# st.markdown('<link rel="stylesheet" href="style/style.css">', unsafe_allow_html=True)

st.sidebar.image("style/logo.png", caption="Анализ на тренировки", use_container_width=True)

users_data = pd.read_csv('data/users_data.csv')
gym_locations_data = pd.read_csv('data/gym_locations_data.csv')
checkin_checkout_history = pd.read_csv('data/checkin_checkout_history_updated.csv')
subscription_plans = pd.read_csv('data/subscription_plans.csv')



checkin_user_data = checkin_checkout_history.merge(users_data, on='user_id')
full_data = checkin_user_data.merge(gym_locations_data, on='gym_id')
checkins_per_gym = full_data['location'].value_counts()




subscription_counts = users_data["subscription_plan"].value_counts().reset_index()
subscription_counts.columns = ["subscription_plan", "count"]





# Създаване на сайдбар
st.sidebar.title("Навигация")





if st.sidebar.button("Анализ"):
    st.write("Тук ще покажем резултатите от анализа.")


    #KARTA
    unique_cities = users_data['user_location'].value_counts().reset_index()
    unique_cities.columns = ['city', 'count']

    # Използваме Geopy за намиране на координати
    geolocator = Nominatim(user_agent="geoapi")
    def get_coordinates(city):
        location = geolocator.geocode(city + ", USA")
        if location:
            return pd.Series([location.latitude, location.longitude])
        return pd.Series([None, None])

    # Добавяне на координати към таблицата с уникални градове
    unique_cities[['latitude', 'longitude']] = unique_cities['city'].apply(get_coordinates)

    # Премахване на градове с липсващи координати
    unique_cities = unique_cities.dropna(subset=['latitude', 'longitude'])


    # Създаване на интерактивна карта с Plotly
    fig = px.scatter_geo(
        unique_cities,
        lat='latitude',
        lon='longitude',
        text='city',
        size='count',
        title='Визуализация на градовете от dataset-а',
        projection='albers usa'
    )

    # fig.show()
    st.plotly_chart(fig)













    # Създаване на графика
    fig = px.bar(
        subscription_counts,
        x="subscription_plan",
        y="count",
        title="Разпределение на абонаментните планове",
        labels={"subscription_plan": "Абонаментен план", "count": "Брой абонати"},
        color="subscription_plan",
    )
    # Задаване на минимална граница на y-ос
    fig.update_yaxes(range=[1600, 1700])  # Минималната стойност е 0, максималната се определя автоматично

    # Показване на графиката в Streamlit
    st.title("Графика на абонаментите")
    st.plotly_chart(fig)

    st.write(users_data)











# Създаване на отделни бутони
if st.sidebar.button("Данни"):
    show_data = True
    st.write("Тук ще покажем данните.")

    st.write(users_data)
    st.write(gym_locations_data)
    st.write(checkin_checkout_history)
    st.write(subscription_plans)




if st.sidebar.button("Информация"):
    st.write("Тук ще покажем допълнителна информация.")


    df = pd.DataFrame({'numbers': [-1, 2, -3, 4]})
    df = df.style.applymap(lambda x: 'color: red' if x < 0 else '')

    st.dataframe(df)


    with st.expander("Скрита информация"):
        st.write("Тук може да поставите скрито съдържание")

    with st.container():
        st.write("Това е в контейнер")



    # Контейнер 1 - Текстово съдържание
    with st.container():
        st.header("Първи контейнер")
        st.write("Това е пример за текстово съдържание в първия контейнер.")
        st.write("Можеш да добавяш колкото си искаш текст тук.")

    # Контейнер 2 - Форма
    with st.container():
        st.header("Втори контейнер - Форма")
        with st.form("my_form"):
            name = st.text_input("Име")
            email = st.text_input("Имейл")
            submitted = st.form_submit_button("Изпрати")
            if submitted:
                st.write("Здравей,", name, "!")

    # Контейнер 3 - Таблица
    with st.container():
        st.header("Трети контейнер - Таблица")
        import pandas as pd
        data = {'име': ['Иван', 'Петър', 'Мария'], 'възраст': [25, 30, 28]}
        df = pd.DataFrame(data)
        st.table(df)
        df = df.reset_index(drop=True)
        
        st.write("Оригинален DataFrame:")
        st.write(df)

        # st.write("DataFrame без индекс:")
        # st.write(st.dataframe(df.style.hide_index()))

        # st.write("Версия на Pandas:", pd.__version__)

        tab1, tab2, tab3 = st.tabs(["Таб 1", "Таб 2", "Таб 3"])

        with tab1:
            st.write("Таб 1 някъв текст примерно.")

        with tab2:
            st.write("Таб 2 някъв текст примерно.")

        with tab3:
            st.write("Таб 3 някъв текст примерно.")

    with st.expander("Виж повече"):
        st.write("Това е допълнителна информация, която се показва при кликване върху заглавието.")
        st.write("Можеш да  текст, изображения или други елементи тук.")



    st.markdown("""
    ## Цели на проекта
    * Карта по градове
    * Възрастови групи
    * Интензивност на тренировки
                    
    `Това е код`
    ### Подзаглавие

    | Колонка 1 | Колонка 2 |
    |---|---|
    | Данни 1 | Данни 2 |
    | Данни 3 | Данни 4 |

    [Link към Google](https://www.google.com)
    """)



# Определяме опциите за филтъра
options = ['Едно', 'Две', 'Три', 'Четири', 'Пет']

with st.sidebar:
    # Добавяме филтъра в страничната лента
    selected_options = st.multiselect('Избери опции:', options)

    # Показваме избраните опции
    st.write('Избрани опции:', selected_options)
