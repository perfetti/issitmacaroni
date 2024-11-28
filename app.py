import streamlit as st
import random

# Dictionary of pasta shapes with their properties
pasta_shapes = {
    "Penne": {
        "image_path": "static/penne.png",
        "description": "Cylinder-shaped pasta with angled ends",
        "is_macaroni": True
    },
    "Spaghetti": {
        "image_path": "static/spaghetti.png",
        "description": "Long, thin, solid pasta",
        "is_macaroni": False
    },
    "Macaroni": {
        "image_path": "static/macaroni.png",
        "description": "Short, curved tubes",
        "is_macaroni": True
    },
    "Farfalle": {
        "image_path": "static/farfalle.png",
        "description": "Bow-tie or butterfly shaped pasta",
        "is_macaroni": False
    },
    "Rigatoni": {
        "image_path": "static/rigatoni.png",
        "description": "Large, tube-shaped pasta with ridges",
        "is_macaroni": True
    },
    "Fusilli": {
        "image_path": "static/fusilli.png",
        "description": "Spiral-shaped pasta",
        "is_macaroni": False
    },
    "Ziti": {
        "image_path": "static/ziti.png",
        "description": "Long, straight tube pasta",
        "is_macaroni": True
    },
    "Cannelloni": {
        "image_path": "static/cannelloni.png",
        "description": "Large, tube-shaped pasta for stuffing",
        "is_macaroni": True
    },
    "Ditalini": {
        "image_path": "static/ditalini.png",
        "description": "Very short tubes, like little thimbles",
        "is_macaroni": True
    },
    "Orecchiette": {
        "image_path": "static/orecchiette.png",
        "description": "Small, ear-shaped pasta",
        "is_macaroni": False
    },
    "Lasagna": {
        "image_path": "static/lasagna.png",
        "description": "Wide, flat sheets of pasta",
        "is_macaroni": False
    },
    "Ravioli": {
        "image_path": "static/ravioli.png",
        "description": "Stuffed pasta squares",
        "is_macaroni": False
    },
    "Torchio": {
        "image_path": "static/torchio.png",
        "description": "Torch-shaped hollow pasta",
        "is_macaroni": True
    },
    "Conchiglie": {
        "image_path": "static/conchiglie.png",
        "description": "Shell-shaped pasta",
        "is_macaroni": False
    },
    "Gemelli": {
        "image_path": "static/gemelli.png",
        "description": "Twisted strand pasta",
        "is_macaroni": False
    },
    "Orzo": {
        "image_path": "static/orzo.png",
        "description": "Rice-shaped pasta",
        "is_macaroni": False
    },
    "Rotelle": {
        "image_path": "static/rotelle.png",
        "description": "Wheel-shaped pasta",
        "is_macaroni": False
    },
    "Tagliatelle": {
        "image_path": "static/tagliatelle.png",
        "description": "Long, flat ribbons of pasta",
        "is_macaroni": False
    },
    "Pappardelle": {
        "image_path": "static/pappardelle.png",
        "description": "Wide, flat ribbons of pasta",
        "is_macaroni": False
    },
    "Bavette": {
        "image_path": "static/bavette.png",
        "description": "Narrow, flat pasta strips",
        "is_macaroni": False
    }
}

def main():
    st.set_page_config(page_title="Is It Macaroni?", layout="centered")

    st.title("Is It Macaroni? 🍝")
    st.write("Macaroni is defined as elongated tubes of pasta, whether straight or curved.")

    # Randomly select a pasta shape if none is in session state
    if 'current_pasta' not in st.session_state:
        st.session_state.current_pasta = random.choice(list(pasta_shapes.keys()))
        st.session_state.answered = False
        st.session_state.score = 0
        st.session_state.total = 0

    # Display the current pasta
    pasta = st.session_state.current_pasta
    st.subheader(f"Is this {pasta} a type of macaroni?")

    # Display the image
    st.image(pasta_shapes[pasta]["image_path"], caption=pasta, width=300)

    st.write(f"Description: {pasta_shapes[pasta]['description']}")

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

    # Next pasta button
    if st.session_state.answered:
        if st.button("Next Pasta"):
            st.session_state.current_pasta = random.choice(list(pasta_shapes.keys()))
            st.session_state.answered = False
            st.experimental_rerun()

def check_answer(user_answer):
    pasta = st.session_state.current_pasta
    correct = pasta_shapes[pasta]["is_macaroni"]

    st.session_state.total += 1
    if user_answer == correct:
        st.success("Correct! 🎉")
        st.session_state.score += 1
    else:
        st.error("Wrong! 😅")

    if correct:
        st.write(f"Yes, {pasta} is a type of macaroni because it's a tubular pasta!")
    else:
        st.write(f"No, {pasta} is not a type of macaroni because it's not a tubular pasta.")

if __name__ == "__main__":
    main()
