from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn

app = FastAPI()

log_reg = joblib.load('model (6).pkl')
tree = joblib.load('tree_model.pkl')
scaler = joblib.load('scaler (6).pkl')

class MushroomSchema(BaseModel):
    cap_shape: str
    cap_surface: str
    cap_color: str
    bruises: str
    odor: str
    gill_attachment: str
    gill_spacing: str
    gill_size: str
    gill_color: str
    stalk_shape: str
    stalk_root: str
    stalk_surface_above_ring: str
    stalk_surface_below_ring: str
    stalk_color_above_ring: str
    stalk_color_below_ring: str
    veil_color: str
    ring_number: str
    ring_type: str
    spore_print_color: str
    population: str
    habitat: str

def build_features(m: MushroomSchema):

    cap_shape = [
        1 if m.cap_shape == "c" else 0,
        1 if m.cap_shape == "f" else 0,
        1 if m.cap_shape == "k" else 0,
        1 if m.cap_shape == "s" else 0,
        1 if m.cap_shape == "x" else 0,
    ]

    cap_surface = [
        1 if m.cap_surface == "g" else 0,
        1 if m.cap_surface == "s" else 0,
        1 if m.cap_surface == "y" else 0,
    ]

    cap_color = [
        1 if m.cap_color == "c" else 0,
        1 if m.cap_color == "e" else 0,
        1 if m.cap_color == "g" else 0,
        1 if m.cap_color == "n" else 0,
        1 if m.cap_color == "p" else 0,
        1 if m.cap_color == "r" else 0,
        1 if m.cap_color == "u" else 0,
        1 if m.cap_color == "w" else 0,
        1 if m.cap_color == "y" else 0,
    ]

    bruises = [1 if m.bruises == "t" else 0]

    odor = [
        1 if m.odor == "c" else 0,
        1 if m.odor == "f" else 0,
        1 if m.odor == "l" else 0,
        1 if m.odor == "m" else 0,
        1 if m.odor == "n" else 0,
        1 if m.odor == "p" else 0,
        1 if m.odor == "s" else 0,
        1 if m.odor == "y" else 0,
    ]

    gill_attachment = [1 if m.gill_attachment == "f" else 0]

    gill_spacing = [1 if m.gill_spacing == "w" else 0]

    gill_size = [1 if m.gill_size == "n" else 0]

    gill_color = [
        1 if m.gill_color == "e" else 0,
        1 if m.gill_color == "g" else 0,
        1 if m.gill_color == "h" else 0,
        1 if m.gill_color == "k" else 0,
        1 if m.gill_color == "n" else 0,
        1 if m.gill_color == "o" else 0,
        1 if m.gill_color == "p" else 0,
        1 if m.gill_color == "r" else 0,
        1 if m.gill_color == "u" else 0,
        1 if m.gill_color == "w" else 0,
        1 if m.gill_color == "y" else 0,
    ]

    stalk_shape = [1 if m.stalk_shape == "t" else 0]

    stalk_root = [
        1 if m.stalk_root == "c" else 0,
        1 if m.stalk_root == "e" else 0,
        1 if m.stalk_root == "r" else 0,
    ]

    stalk_surface_above = [
        1 if m.stalk_surface_above_ring == "k" else 0,
        1 if m.stalk_surface_above_ring == "s" else 0,
        1 if m.stalk_surface_above_ring == "y" else 0,
    ]

    stalk_surface_below = [
        1 if m.stalk_surface_below_ring == "k" else 0,
        1 if m.stalk_surface_below_ring == "s" else 0,
        1 if m.stalk_surface_below_ring == "y" else 0,
    ]

    stalk_color_above = [
        1 if m.stalk_color_above_ring == "c" else 0,
        1 if m.stalk_color_above_ring == "e" else 0,
        1 if m.stalk_color_above_ring == "g" else 0,
        1 if m.stalk_color_above_ring == "n" else 0,
        1 if m.stalk_color_above_ring == "o" else 0,
        1 if m.stalk_color_above_ring == "p" else 0,
        1 if m.stalk_color_above_ring == "w" else 0,
        1 if m.stalk_color_above_ring == "y" else 0,
    ]

    stalk_color_below = [
        1 if m.stalk_color_below_ring == "c" else 0,
        1 if m.stalk_color_below_ring == "e" else 0,
        1 if m.stalk_color_below_ring == "g" else 0,
        1 if m.stalk_color_below_ring == "n" else 0,
        1 if m.stalk_color_below_ring == "o" else 0,
        1 if m.stalk_color_below_ring == "p" else 0,
        1 if m.stalk_color_below_ring == "w" else 0,
        1 if m.stalk_color_below_ring == "y" else 0,
    ]

    veil_color = [
        1 if m.veil_color == "o" else 0,
        1 if m.veil_color == "w" else 0,
        1 if m.veil_color == "y" else 0,
    ]

    ring_number = [
        1 if m.ring_number == "o" else 0,
        1 if m.ring_number == "t" else 0,
    ]

    ring_type = [
        1 if m.ring_type == "f" else 0,
        1 if m.ring_type == "l" else 0,
        1 if m.ring_type == "n" else 0,
        1 if m.ring_type == "p" else 0,
    ]

    spore_print = [
        1 if m.spore_print_color == "h" else 0,
        1 if m.spore_print_color == "k" else 0,
        1 if m.spore_print_color == "n" else 0,
        1 if m.spore_print_color == "o" else 0,
        1 if m.spore_print_color == "r" else 0,
        1 if m.spore_print_color == "u" else 0,
        1 if m.spore_print_color == "w" else 0,
        1 if m.spore_print_color == "y" else 0,
    ]

    population = [
        1 if m.population == "c" else 0,
        1 if m.population == "n" else 0,
        1 if m.population == "s" else 0,
        1 if m.population == "v" else 0,
        1 if m.population == "y" else 0,
    ]

    habitat = [
        1 if m.habitat == "g" else 0,
        1 if m.habitat == "l" else 0,
        1 if m.habitat == "m" else 0,
        1 if m.habitat == "p" else 0,
        1 if m.habitat == "u" else 0,
        1 if m.habitat == "w" else 0,
    ]

    return (
        cap_shape
        + cap_surface
        + cap_color
        + bruises
        + odor
        + gill_attachment
        + gill_spacing
        + gill_size
        + gill_color
        + stalk_shape
        + stalk_root
        + stalk_surface_above
        + stalk_surface_below
        + stalk_color_above
        + stalk_color_below
        + veil_color
        + ring_number
        + ring_type
        + spore_print
        + population
        + habitat
    )


@app.post('/predict-logistic')
async def predict_logistic(m: MushroomSchema):
    features = build_features(m)
    scaled_data = scaler.transform([features])
    pred = log_reg.predict(scaled_data)[0]
    prob = log_reg.predict_proba(scaled_data)[0][1]

    return {'poisonous': bool(pred), 'probability': float(prob)}

@app.post('/predict-tree')
async def predict_tree(m: MushroomSchema):
    features = build_features(m)
    pred = tree.predict([features])[0]
    prob = tree.predict_proba([features])[0][1]

    return {'poisonous': bool(pred), 'probability': float(prob)}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)