import requests
import streamlit as st

api_log = 'http://127.0.0.1:8000/predict-logistic'
api_tree = 'http://127.0.0.1:8000/predict-tree'

st.title('Mushroom Model')

cap_shape = st.selectbox('Cap shape', ["c", "f", "k", "s", "x"])
cap_surface = st.selectbox('Cap surface', ["g", "s", "y"])
cap_color = st.selectbox('Cap color', ["c", "e", "g", "n", "p", "r", "u", "w", "y"])
bruises = st.selectbox('Bruises', ["t", "f"])
odor = st.selectbox('Odor', ["c", "f", "l", "m", "n", "p", "s", "y"])
gill_attachment = st.selectbox('Gill attachment', ["f", "a"])
gill_spacing = st.selectbox('Gill spacing', ["w", "c"])
gill_size = st.selectbox('Gill size', ["n", "b"])
gill_color = st.selectbox('Gill color', ["e", "g", "h", "k", "n", "o", "p", "r", "u", "w", "y"])
stalk_shape = st.selectbox('Stalk shape', ["t", "e"])
stalk_root = st.selectbox('Stalk root', ["c", "e", "r"])
stalk_surface_above_ring = st.selectbox('Stalk surface above ring', ['k', 's', 'y'])
stalk_surface_below_ring = st.selectbox('Stalk surface below ring', ['k', 's', 'y'])
stalk_color_above_ring = st.selectbox('Stalk color above ring', ["c", "e", "g", "n", "o", "p", "w", "y"])
stalk_color_below_ring = st.selectbox('Stalk color below ring', ["c", "e", "g", "n", "o", "p", "w", "y"])
veil_color = st.selectbox('Veil color', ["o", "w", "y"])
ring_number = st.selectbox('Ring number', ['o', 't'])
ring_type = st.selectbox('Ring type', ['f', 'l', 'n', 'p'])
spore_print_color = st.selectbox('Spore print color', ['h', 'k', 'n', 'o', 'r', 'u', 'w', 'y'])
population = st.selectbox('Population', ['c', 'n', 's', 'v', 'y'])
habitat = st.selectbox('Habitat', ['g', 'l', 'm', 'p', 'u', 'w'])

model_type = st.selectbox('Model', ['logistic', 'tree'])

mushroom_dict = {
    'cap_shape': cap_shape,
    'cap_surface': cap_surface,
    'cap_color': cap_color,
    'bruises': bruises,
    'odor': odor,
    'gill_attachment': gill_attachment,
    'gill_spacing': gill_spacing,
    'gill_size': gill_size,
    'gill_color': gill_color,
    'stalk_shape': stalk_shape,
    'stalk_root': stalk_root,
    'stalk_surface_above_ring': stalk_surface_above_ring,
    'stalk_surface_below_ring': stalk_surface_below_ring,
    'stalk_color_above_ring': stalk_color_above_ring,
    'stalk_color_below_ring': stalk_color_below_ring,
    'veil_color': veil_color,
    'ring_number': ring_number,
    'ring_type': ring_type,
    'spore_print_color': spore_print_color,
    'population': population,
    'habitat': habitat
}

if st.button('Check'):
    try:
        url = api_log if model_type == 'logistic' else api_tree
        request = requests.post(url, json=mushroom_dict)

        if request.status_code == 200:
            result = request.json()
            st.json(result)
        else:
            st.error(f'Error: {request.status_code}')
    except requests.exceptions.RequestException:
        st.error('Can not connect to the api')