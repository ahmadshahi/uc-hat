from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code


def question_demo() -> None:
    # Define the questions and options based on the decision tree provided
    questions = {
        "Q1": "As you prepare your garden for the upcoming dry season in New Zealand, which primary area will you focus on first?",
        "Q2": "What specific aspect of soil moisture management will you address?",
        "Q3": "Which water conservation strategy will you prioritize?",
        "Q4": "What focus will you take in selecting and managing your crops?",
        "Q5": "How will you improve water retention in your soil?",
        "Q6": "To reduce evaporation, which technique will you use?",
        "Q7": "How will you optimize your garden's layout for dry conditions?",
        "Q8": "How will you enhance irrigation efficiency?",
        "Q9": "What alternative water sources will you utilize?",
        "Q10": "Which water-saving gardening technique will you implement?",
        "Q11": "How will you utilize drought-resistant crops?",
        "Q12": "How will you adjust planting strategies?",
        "Q13": "What organic materials will you incorporate to enhance water retention?",
        "Q14": "How will you construct swales effectively?",
        "Q15": "Which mulching technique will you adopt?",
        "Q16": "How will you design to minimize wind exposure?",
        "Q17": "What will be your focus when installing drip irrigation?",
        "Q18": "How will you optimize watering schedules?",
        "Q19": "How will you implement rainwater harvesting?",
        "Q20": "What dry farming techniques will you practice?",
        "Q21": "How will you use water retention granules?",
        "Q22": "What soil management practices will you combine with drought-resistant crops?",
        "Q23": "What will you focus on with raised beds?",
        "Q24": "How will you use biochar effectively?",
        "Q25": "How will you integrate permaculture insights into swale design?"
    }

    options = {
        "Q1": {"a": ("Soil moisture management", "Q2"),
               "b": ("Water conservation strategies", "Q3"),
               "c": ("Crop selection and management", "Q4"),
               "d": ("Garden layout optimization", "Q4")},
        "Q2": {"a": ("Improving water retention in the soil", "Q5"),
               "b": ("Reducing evaporation rates from the soil surface", "Q6")},
        "Q3": {"a": ("Enhancing irrigation efficiency", "Q8"),
               "b": ("Utilizing alternative water sources", "Q9"),
               "c": ("Implementing water-saving gardening techniques", "Q10")},
        "Q4": {"a": ("Selecting drought-resistant crop varieties", "Q11"),
               "b": ("Adjusting planting dates and methods to suit dry conditions", "Q12")},
        "Q5": {"a": ("Incorporating organic matter into the soil", "Q13"),
               "b": ("Using soil covers to reduce surface exposure", "A"),
               "c": ("Constructing soil swales to enhance infiltration", "Q14")},
        "Q6": {"a": ("Applying mulches to cover soil surface", "Q15"),
               "b": ("Implementing shading strategies to lower soil temperature", "C")},
        "Q7": {"a": ("Designing the layout to minimize wind exposure", "Q16"),
               "b": ("Creating microclimates that conserve moisture", "B")},
        "Q8": {"a": ("Installing drip irrigation systems", "Q17"),
               "b": ("Optimizing watering schedules based on weather forecasts", "Q18")},
        "Q9": {"a": ("Setting up rainwater harvesting systems", "Q19"),
               "b": ("Exploring groundwater use possibilities", "C")},
        "Q10": {"a": ("Practicing dry farming techniques", "Q20"),
                "b": ("Using water retention granules", "Q21")},
        "Q11": {"a": ("Integrating permaculture principles with these crops", "B"),
                "b": ("Combining these crops with effective soil management practices", "Q22")},
        "Q12": {"a": ("Staggering planting times to optimize growth phases", "A"),
                "b": ("Using raised beds to enhance drainage and aeration", "Q23")},
        "Q13": {"a": ("Adding biochar to improve soil structure", "Q24"),
                "b": ("Using compost to increase organic content", "C")},
        "Q14": {"a": ("Positioning swales along contour lines to maximize water catchment", "Q25"),
                "b": ("Designing swales with permaculture insights to optimize efficiency", "B")},
        "Q15": {"a": ("Using straw to cover larger areas efficiently", "B"),
                "b": ("Utilizing wood chips for longer-lasting soil coverage", "C"),
                "c": ("Applying leaf mold to enhance soil fertility along with coverage", "A")},
        "Q16": {"a": ("Planting windbreaks using native species", "A"),
                "b": ("Constructing artificial barriers", "C"),
                "c": ("Using topography to natural advantage", "B")},
        "Q17": {"a": ("Customizing emitter placement to match plant requirements", "A"),
                "b": ("Automating the system for optimal water use", "B"),
                "c": ("Ensuring minimal leakage and high efficiency", "C")},
        "Q18": {"a": ("Using soil moisture sensors to determine watering needs", "B"),
                "b": ("Integrating a weather-responsive irrigation controller", "A"),
                "c": ("Manually adjusting schedules based on weekly weather reports", "C")},
        "Q19": {"a": ("Constructing underground storage tanks", "B"),
                "b": ("Using above-ground barrels for ease of access and maintenance", "A")},
        "Q20": {"a": ("Reducing tillage to preserve soil moisture", "C"),
                "b": ("Increasing plant spacing to reduce competition for water", "B"),
                "c": ("Choosing specific crops that require less water", "A")},
        "Q21": {"a": ("Mixing granules with soil at root zones", "A"),
                "b": ("Applying granules in potted plants for controlled hydration", "B"),
                "c": ("Dispersing granules across open fields to manage moisture uniformly", "C")},
        "Q22": {"a": ("Implementing no-till methods to maintain soil structure", "A"),
                "b": ("Cycling cover crops to enrich the soil", "B")},
        "Q23": {"a": ("Ensuring good soil mix to maximize water efficiency", "C"),
                "b": ("Using green manures to maintain soil health", "A")},
        "Q24": {"a": ("Blending biochar with compost for synergistic effects", "C"),
                "b": ("Applying biochar in layers to optimize nutrient absorption", "A"),
                "c": ("Incorporating biochar during the planting season to aid in water retention", "B")},
        "Q25": {"a": ("Incorporating edible perennials along swales", "A"),
                "b": ("Using swales to create biodiversity hotspots", "C"),
                "c": ("Designing swales to double as pathways for farm access", "B")}
    }

    # Initialize session state to track user choices and current question
    if 'current_question' not in st.session_state:
        st.session_state['current_question'] = 'Q1'
        st.session_state['user_responses'] = {}
        st.session_state['selected_option'] = None  # Placeholder for the selected option

    def navigate_questions():
        # Save the user's choice
        option_selected = st.session_state['selected_option']
        next_q = options[st.session_state['current_question']][option_selected][1]

        # Update responses
        st.session_state.user_responses[st.session_state['current_question']] = option_selected

        # Check if it's an endpoint
        if next_q in ['A', 'B', 'C']:
            st.session_state['current_question'] = None  # Clear current question
            st.session_state['final_outcome'] = next_q
            st.session_state['endpoint_reached'] = True
        else:
            st.session_state['current_question'] = next_q  # Update to the next question
            st.session_state['selected_option'] = None  # Reset selected option for the next question

    # Display the current question
    current_question = st.session_state['current_question']
    if current_question and not st.session_state.get('endpoint_reached', False):
        # Radio buttons for options
        options_list = [(f"{k}: {v[0]}", k) for k, v in options[current_question].items()]
        selected = st.radio(f"{current_question}) {questions[current_question]}", options_list,
                            format_func=lambda x: x[0], index=None, key=f'{current_question}_radio')

        # Update the selected option in session state
        if selected:
            st.session_state['selected_option'] = selected[1]

        # Enable the Next button only if an option is selected
        if st.session_state['selected_option']:
            if st.button("Next", key=f'{current_question}_next'):
                navigate_questions()

    # Handle endpoint reached
    if 'endpoint_reached' in st.session_state and st.session_state['endpoint_reached']:
        st.write(f"You've reached the end of the survey with outcome: {st.session_state['final_outcome']}")
        if st.button("Submit"):
            st.write("Responses submitted:", st.session_state.user_responses)
            # Clear session state for a new survey run
            st.session_state.clear()


st.set_page_config(page_title="Animation Demo", page_icon="📹")
st.markdown("# Animation Demo")
st.sidebar.header("Animation Demo")
st.write(
    """This app shows how you can use Streamlit to build cool animations.
It displays an animated fractal based on the the Julia Set. Use the slider
to tune different parameters."""
)

question_demo()

show_code(question_demo)