import streamlit as st

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Speak Up & Challenge Hub",
    page_icon="💬",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #fafafa;
    }

    h1, h2, h3 {
        color: #2b164d;
    }

    .hero-box {
        background: linear-gradient(135deg, #2b164d, #5e2ca5);
        padding: 35px;
        border-radius: 18px;
        color: white;
        margin-bottom: 25px;
    }

    .hero-box h1 {
        color: white;
        font-size: 42px;
        margin-bottom: 10px;
    }

    .hero-box p {
        font-size: 18px;
        line-height: 1.5;
    }

    .info-card {
        background-color: white;
        padding: 22px;
        border-radius: 14px;
        border-left: 6px solid #5e2ca5;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        margin-bottom: 18px;
    }

    .small-card {
        background-color: #ffffff;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e6e6e6;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 15px;
    }

    .value-card {
        background-color: #f2ecff;
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 15px;
        border: 1px solid #ded1ff;
    }

    .footer-note {
        color: #666666;
        font-size: 14px;
        margin-top: 35px;
    }

    .tag {
        display: inline-block;
        background-color: #eee6ff;
        color: #2b164d;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        margin-right: 6px;
        margin-bottom: 6px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar navigation
# -----------------------------
st.sidebar.title("Speak Up & Challenge Hub")
st.sidebar.caption("Digital selling tool prototype")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Why this tool is needed",
        "Team Kick-Off Card",
        "Speak-Up Phrase Bank",
        "Manager Reflection Card",
        "Implementation Guide",
        "Business Value"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Target group: audit associates, seniors, junior managers, and managers "
    "working in multicultural audit teams."
)

# -----------------------------
# Home page
# -----------------------------
if page == "Home":
    st.markdown(
        """
        <div class="hero-box">
            <h1>Speak Up & Challenge Hub</h1>
            <p>
            A practical digital tool for improving communication, professional skepticism,
            and audit quality in multicultural audit teams.
            </p>
            <p><strong>Designed for:</strong> International Audit Teams</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <span class="tag">Intercultural Communication</span>
        <span class="tag">Professional Skepticism</span>
        <span class="tag">Audit Quality</span>
        <span class="tag">Psychological Safety</span>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="info-card">
                <h3>Topic</h3>
                <p>
                This tool focuses on intercultural communication, professional skepticism,
                and audit quality within multicultural audit teams.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="info-card">
                <h3>Context</h3>
                <p>
                The tool is designed for international and multicultural audit teams
                all over the world, especially in situations where language differences and cultural communication styles may influence how team members speak up and challenge audit evidence.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="info-card">
                <h3>Target Group</h3>
                <p>
                Audit associates, seniors, junior managers, and managers working in
                multicultural audit teams.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="info-card">
                <h3>Scope</h3>
                <p>
                Practical use during audit engagements, especially kick-off meetings,
                fieldwork communication, review moments, and engagement evaluations.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("Key terminology")

    terms = {
        "Intercultural communication": "How people from different cultural and language backgrounds exchange information and interpret messages.",
        "Professional skepticism": "A questioning mindset and critical assessment of audit evidence.",
        "Audit quality": "The extent to which the audit is performed effectively, consistently, and in line with professional standards.",
        "Psychological safety": "The feeling that team members can ask questions, raise concerns, and challenge ideas without fear of embarrassment or negative consequences."
    }

    for term, definition in terms.items():
        st.markdown(
            f"""
            <div class="small-card">
                <strong>{term}</strong><br>
                {definition}
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------
# Why this tool is needed
# -----------------------------
elif page == "Why this tool is needed":
    st.title("Why this tool is needed")

    st.markdown(
        """
        <div class="info-card">
            <h3>Research-based problem</h3>
            <p>
            Research shows that language differences, cultural communication styles,
            hierarchy, and confidence can influence how team members communicate and
            whether they feel comfortable expressing professional skepticism.
            </p>
            <p>
            In multicultural audit teams, important doubts or alternative views may
            remain unspoken when communication expectations are unclear.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Main communication risks")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="small-card">
                <h4>Language differences</h4>
                <p>Team members may hesitate to speak when they are unsure how to phrase a concern.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="small-card">
                <h4>Cultural styles</h4>
                <p>Direct and indirect communication styles can lead to misunderstanding.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="small-card">
                <h4>Hierarchy</h4>
                <p>Junior team members may avoid challenging seniors or managers.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class="small-card">
                <h4>Confidence</h4>
                <p>Team members may doubt whether their concern is important enough to raise.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("Conclusion")

    st.success(
        "Clear communication and psychologically safe challenge moments strengthen "
        "professional skepticism and help teams make better audit judgments."
    )

# -----------------------------
# Team Kick-Off Card
# -----------------------------
elif page == "Team Kick-Off Card":
    st.title("Team Kick-Off Card")

    st.markdown(
        """
        <div class="info-card">
            <h3>Purpose</h3>
            <p>
            The Team Kick-Off Card helps audit teams agree on communication norms
            before the audit work begins.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Kick-off discussion questions")

    questions = [
        "How will we make sure everyone can ask questions or raise concerns?",
        "What is the best way to challenge audit evidence respectfully in this team?",
        "How will we handle language differences or unclear explanations?",
        "When should team members escalate doubts or uncertainty?",
        "How will seniors and managers invite input from quieter team members?"
    ]

    completed = []

    for question in questions:
        answer = st.checkbox(question)
        completed.append(answer)

    progress = sum(completed) / len(completed)
    st.progress(progress)

    st.write(f"Checklist progress: **{sum(completed)} / {len(completed)} completed**")

    st.subheader("Team agreement")

    st.write("Use this section during the engagement kick-off.")

    agreement_1 = st.text_input("In this engagement, we agree to...")
    agreement_2 = st.text_input("We will raise concerns by...")
    agreement_3 = st.text_input("We will escalate unresolved doubts when...")

    if st.button("Generate team agreement"):
        st.markdown("### Draft team agreement")
        st.write(f"1. In this engagement, we agree to: **{agreement_1 or '[add agreement]'}**")
        st.write(f"2. We will raise concerns by: **{agreement_2 or '[add agreement]'}**")
        st.write(f"3. We will escalate unresolved doubts when: **{agreement_3 or '[add agreement]'}**")

# -----------------------------
# Speak-Up Phrase Bank
# -----------------------------
elif page == "Speak-Up Phrase Bank":
    st.title("Speak-Up Phrase Bank")

    st.markdown(
        """
        <div class="info-card">
            <h3>Purpose</h3>
            <p>
            The Speak-Up Phrase Bank gives team members practical sentence starters
            for raising concerns, asking questions, and challenging audit evidence respectfully.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    phrases = {
        "Asking for clarification": [
            "Could you explain the reasoning behind this conclusion?",
            "Can we walk through how this evidence supports the conclusion?",
            "Could you clarify what assumption we are relying on here?"
        ],
        "Challenging evidence": [
            "I may be missing something, but this evidence does not fully support the conclusion yet.",
            "Can we check whether this evidence is sufficient and appropriate?",
            "I think we may need stronger support before finalizing this conclusion."
        ],
        "Raising uncertainty": [
            "I am not fully comfortable with this assumption. Can we review it together?",
            "I am uncertain whether we have addressed this risk completely.",
            "This point may need more discussion before we move forward."
        ],
        "Offering an alternative view": [
            "Another way to look at this risk could be...",
            "Could there be another explanation for this result?",
            "Would it be useful to consider a different perspective?"
        ],
        "Escalating respectfully": [
            "I think this point may require manager input before we proceed.",
            "This issue may be important enough to discuss during the review meeting.",
            "Can we involve the manager to make sure we are aligned?"
        ],
        "Inviting others in": [
            "Does anyone see this differently or have concerns we have not discussed yet?",
            "Would anyone like to add another perspective?",
            "Before we conclude, are there any doubts or alternative views?"
        ]
    }

    situation = st.selectbox("Choose a situation", list(phrases.keys()))

    st.subheader("Useful phrases")

    for phrase in phrases[situation]:
        st.markdown(
            f"""
            <div class="small-card">
                “{phrase}”
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("Create your own phrase")

    custom_context = st.text_area(
        "Describe the concern you want to raise",
        placeholder="Example: I am not sure whether the audit evidence is strong enough."
    )

    if st.button("Create respectful speak-up sentence"):
        if custom_context.strip():
            st.success(
                f"Suggested phrase: I would like to raise one point for discussion. "
                f"{custom_context.strip()} Could we review this together before we proceed?"
            )
        else:
            st.warning("Please describe the concern first.")

# -----------------------------
# Manager Reflection Card
# -----------------------------
elif page == "Manager Reflection Card":
    st.title("Manager Reflection Card")

    st.markdown(
        """
        <div class="info-card">
            <h3>Purpose</h3>
            <p>
            This card helps seniors, junior managers, and managers reflect on whether
            they created enough space for team members to speak up and challenge evidence.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Reflection questions")

    reflection_questions = [
        "Did I actively invite questions and different viewpoints?",
        "Did I make it clear that challenge is expected, not personal?",
        "Did language or hierarchy prevent someone from contributing?",
        "Did I respond constructively when someone raised a concern?",
        "Did the team document and follow up on important doubts?"
    ]

    scores = {}

    for question in reflection_questions:
        scores[question] = st.slider(question, 1, 5, 3)

    average_score = sum(scores.values()) / len(scores)

    st.subheader("Reflection score")

    st.metric("Average reflection score", f"{average_score:.1f} / 5")

    if average_score >= 4:
        st.success("Strong reflection result. The team environment appears supportive of speaking up.")
    elif average_score >= 3:
        st.warning("Moderate result. There may be opportunities to invite more challenge and input.")
    else:
        st.error("Attention needed. Speaking up may not be sufficiently supported in this team environment.")

    st.subheader("Action for next review meeting")

    action = st.text_area(
        "One action I will take in the next review meeting is...",
        placeholder="Example: I will ask each team member whether they see any risk or evidence differently."
    )

    if st.button("Save reflection summary"):
        st.markdown("### Reflection summary")
        st.write(f"Average score: **{average_score:.1f} / 5**")
        st.write(f"Next action: **{action or '[add action]'}**")

# -----------------------------
# Implementation Guide
# -----------------------------
elif page == "Implementation Guide":
    st.title("Implementation Guide")

    st.markdown(
        """
        <div class="info-card">
            <h3>How to use the Speak Up & Challenge Hub</h3>
            <p>
            The tool is designed for practical use during different stages of the audit engagement.
            It helps teams make communication expectations explicit and supports consistent
            professional skepticism.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    implementation_data = {
        "Moment": [
            "Engagement kick-off",
            "During fieldwork",
            "Review meetings",
            "Engagement evaluation"
        ],
        "Who uses it": [
            "Whole team",
            "Associates and seniors",
            "Seniors, junior managers, and managers",
            "Whole team"
        ],
        "How to use it": [
            "Discuss the Team Kick-Off Card and agree on communication norms.",
            "Use the Speak-Up Phrase Bank when raising questions or challenging evidence.",
            "Use the Manager Reflection Card to check whether input was invited and concerns were followed up.",
            "Discuss what helped or blocked open communication and professional skepticism."
        ]
    }

    st.table(implementation_data)

    st.subheader("Recommended use during an audit engagement")

    st.markdown(
        """
        1. Start the engagement with the **Team Kick-Off Card**.  
        2. Use the **Speak-Up Phrase Bank** during fieldwork and evidence discussions.  
        3. Apply the **Manager Reflection Card** before or after review meetings.  
        4. Revisit the tool during the engagement evaluation to identify improvements.
        """
    )

# -----------------------------
# Business Value
# -----------------------------
elif page == "Business Value":
    st.title("Business Value")

    st.markdown(
        """
        <div class="info-card">
            <h3>Why this tool adds value</h3>
            <p>
            The Speak Up & Challenge Hub translates research findings into a practical
            digital solution for international audit teams. It supports clearer communication,
            stronger professional skepticism, and better audit quality.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    values = [
        {
            "title": "Supports professional skepticism",
            "text": "The tool gives team members practical ways to question assumptions and challenge audit evidence respectfully."
        },
        {
            "title": "Reduces misunderstandings",
            "text": "Clear communication expectations help reduce confusion caused by language, hierarchy, or cultural communication styles."
        },
        {
            "title": "Improves review quality",
            "text": "Managers and seniors are encouraged to invite input, document doubts, and follow up on important concerns."
        },
        {
            "title": "Strengthens teamwork",
            "text": "The tool supports psychological safety by making speaking up a normal and expected part of the audit process."
        },
        {
            "title": "Scalable for international audit teams",
            "text": "The digital format can be reused across engagements, teams, and offices."
        }
    ]

    for value in values:
        st.markdown(
            f"""
            <div class="value-card">
                <h3>{value["title"]}</h3>
                <p>{value["text"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success(
        "Overall conclusion: By making communication expectations explicit, the tool helps "
        "multicultural audit teams speak up, challenge evidence, and support audit quality."
    )

# -----------------------------
# Footer inside app
# -----------------------------
st.markdown(
    """
    <p class="footer-note">
    Prototype developed as a selling tool for a research project on intercultural communication,
    professional skepticism, and audit quality in multicultural audit teams.
    </p>
    """,
    unsafe_allow_html=True
)