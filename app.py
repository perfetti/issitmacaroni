import streamlit as st
import random

# Dictionary of shapes with their properties
shapes = {
    "Penne": {
        "image_path": "static/penne.png",
        "description": "Cylinder-shaped pasta with angled ends",
        "is_macaroni": True,
        "technically": None
    },
    "Spaghetti": {
        "image_path": "static/spaghetti.png",
        "description": "Long, thin, solid pasta",
        "is_macaroni": False,
        "technically": None
    },
    "Macaroni": {
        "image_path": "static/macaroni.png",
        "description": "Short, curved tubes",
        "is_macaroni": True,
        "technically": None
    },
    "Farfalle": {
        "image_path": "static/farfalle.png",
        "description": "Bow-tie or butterfly shaped pasta",
        "is_macaroni": False,
        "technically": None
    },
    "Rigatoni": {
        "image_path": "static/rigatoni.png",
        "description": "Large, tube-shaped pasta with ridges",
        "is_macaroni": True,
        "technically": None
    },
    "Fusilli": {
        "image_path": "static/fusilli.png",
        "description": "Spiral-shaped pasta",
        "is_macaroni": False,
        "technically": None
    },
    "Ziti": {
        "image_path": "static/ziti.png",
        "description": "Long, straight tube pasta",
        "is_macaroni": True,
        "technically": None
    },
    "Cannelloni": {
        "image_path": "static/cannelloni.png",
        "description": "Large, tube-shaped pasta for stuffing",
        "is_macaroni": True,
        "technically": None
    },
    "Ditalini": {
        "image_path": "static/ditalini.png",
        "description": "Very short tubes, like little thimbles",
        "is_macaroni": True,
        "technically": None
    },
    "The Subway": {
        "image_path": "static/subway.png",
        "description": "The Subway is a long, tubular structure but due to structural requirements, it couldn't be considered a type of macaroni",
        "is_macaroni": False
    },
    "Snake": {
        "image_path": "static/snake.png",
        "description": "A long, cylindrical reptile",
        "is_macaroni": False,
        "technically": "If you were to cook a snake (please don't), it would form a tube-like structure similar to macaroni"
    },
    "Bamboo": {
        "image_path": "static/bamboo.png",
        "description": "A naturally hollow plant stem",
        "is_macaroni": False,
        "technically": "Bamboo is naturally tubular and if prepared properly (though not recommended), could technically function like a very large macaroni"
    },
    "Pen": {
        "image_path": "static/pen.png",
        "description": "A writing instrument",
        "is_macaroni": False,
        "technically": "A hollow pen tube, if made of edible materials, would technically be a macaroni-like structure"
    },
    "Wave": {
        "image_path": "static/wave.png",
        "description": "A curling ocean wave",
        "is_macaroni": False,
        "technically": "When a wave curls, it briefly forms a perfect tube shape, making it a temporary water macaroni"
    },
    "Orecchiette": {
        "image_path": "static/orecchiette.png",
        "description": "Small, ear-shaped pasta",
        "is_macaroni": False,
        "technically": None
    },
    "Lasagna": {
        "image_path": "static/lasagna.png",
        "description": "Wide, flat sheets of pasta",
        "is_macaroni": False,
        "technically": None
    },
    "Ravioli": {
        "image_path": "static/ravioli.png",
        "description": "Stuffed pasta squares",
        "is_macaroni": False,
        "technically": None
    },
    "Torchio": {
        "image_path": "static/torchio.png",
        "description": "Torch-shaped hollow pasta",
        "is_macaroni": True,
        "technically": None
    }
}

def main():
    st.set_page_config(page_title="Is It Macaroni?", layout="centered")

    st.title("Is It Macaroni? 🍝")
    st.write("Macaroni is defined as elongated tubes of pasta, whether straight or curved.")

    # Randomly select a shape if none is in session state
    if 'current_shape' not in st.session_state:
        st.session_state.current_shape = random.choice(list(shapes.keys()))
        st.session_state.answered = False
        st.session_state.score = 0
        st.session_state.total = 0

    # Display the current shape
    shape = st.session_state.current_shape
    st.subheader(f"Is this {shape} a type of macaroni?")

    # Display the image
    st.image(shapes[shape]["image_path"], caption=shape, width=300)

    st.write(f"Description: {shapes[shape]['description']}")

    # Get user input
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, it's macaroni!") and not st.session_state.answered:
            user_answer = True
            st.session_state.answered = True
            check_answer(user_answer)

    with col2:
        if st.button("No, not macaroni!") and not st.session_state.answered:
            user_answer = False
            st.session_state.answered = True
            check_answer(user_answer)

    # Display score
    st.write(f"Score: {st.session_state.score}/{st.session_state.total}")

    # Next shape button
    if st.session_state.answered:
        if st.button("Next Shape"):
            st.session_state.current_shape = random.choice(list(shapes.keys()))
            st.session_state.answered = False
            st.experimental_rerun()

def check_answer(user_answer):
    shape = st.session_state.current_shape
    correct = shapes[shape]["is_macaroni"]
    technically = shapes[shape].get("technically")  # Using .get() to safely handle missing key

    st.session_state.total += 1

    # If there's a technicality, both answers are correct
    if technically:
        st.success("Correct! 🎉")
        st.session_state.score += 1
        if user_answer:
            st.write(f"Yes, {shape} could technically be considered a type of macaroni!")
        else:
            st.write(f"No, {shape} is not traditionally considered a type of macaroni.")
        st.info(f"Here's why both answers work: {technically}")
    else:
        # Regular scoring for non-technical items
        if user_answer == correct:
            st.success("Correct! 🎉")
            st.session_state.score += 1
            if correct:
                st.write(f"Yes, {shape} is a type of macaroni because it's a tubular pasta!")
            else:
                st.write(f"No, {shape} is not a type of macaroni because it's not a tubular pasta.")
        else:
            st.error("Wrong! 😅")
            if correct:
                st.write(f"Actually, {shape} is a type of macaroni because it's a tubular pasta!")
            else:
                st.write(f"No, {shape} is not a type of macaroni because it's not a tubular pasta.")

if __name__ == "__main__":
    main()
