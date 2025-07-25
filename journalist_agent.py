
# Import the required libraries
from textwrap import dedent
from agno.agent import Agent
from agno.tools.serpapi import SerpApiTools
from agno.tools.newspaper4k import Newspaper4kTools
import streamlit as st
from agno.models.openai import OpenAIChat



# Inject vibrant dark theme and animated, colorful UI
st.markdown(
    """
    <style>
    body, .main, .block-container {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        color: #f8fafc;
    }
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
    }
    .stTitle, .stCaption, .stSubheader, .stMarkdown, .stTextInput, .stSelectbox, .stMultiselect, .stButton, .stSlider, .stTextArea {
        color: #f8fafc !important;
    }
    .stSidebar .sidebar-content {
        background: linear-gradient(135deg, #232526 0%, #414345 100%);
        color: #ffd200;
        border-radius: 16px;
        box-shadow: 0 2px 24px #00c6ff;
        padding: 24px 8px 8px 8px;
        margin-bottom: 24px;
    }
    .sidebar-logo {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 24px;
        animation: fadeIn 1.5s;
    }
    .sidebar-logo img {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        box-shadow: 0 4px 24px #ffd200;
        border: 4px solid #00c6ff;
        margin-bottom: 12px;
        background: #232526;
        object-fit: cover;
    }
    .sidebar-logo span {
        color: #ffd200;
        font-size: 1.3em;
        font-family: monospace;
        font-weight: bold;
        text-shadow: 0 2px 12px #00c6ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar logo with unique style
import os
import base64
logo_path = os.path.join(os.path.dirname(__file__), "Logo.png")
with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()
st.sidebar.markdown(
    f"""
    <div class='sidebar-logo'>
        <img src='data:image/png;base64,{encoded_logo}' alt='Logo'>
        <span>NewsCraft.AI</span>
    </div>
    """,
    unsafe_allow_html=True
)
# Add a second logo below the previous one in the sidebar
st.sidebar.markdown(
    f"""
    <div class='sidebar-logo' style='margin-top:0;'>
        <img src='data:image/png;base64,{encoded_logo}' alt='Logo' style='width:210px;height:220px;border-radius:30%;box-shadow:0 2px 12px #00c6ff;border:2px solid #ffd200;margin-bottom:8px;background:#232526;object-fit:cover;'>
        <span style='color:#00c6ff;font-size:1.1em;font-family:sans-serif;font-weight:bold;text-shadow:0 1px 6px #ffd200;'></span>
    </div>
    """,
    unsafe_allow_html=True
)


# Add a third logo below the previous one in the app
st.markdown(
    f"""
    <style>
    @keyframes colorfulGlow {{
        0% {{ box-shadow: 0 0 24px #ffd200, 0 0 0px #00c6ff; filter: hue-rotate(0deg); }}
        25% {{ box-shadow: 0 0 32px #00c6ff, 0 0 12px #f7971e; filter: hue-rotate(90deg); }}
        50% {{ box-shadow: 0 0 40px #f7971e, 0 0 24px #ffd200; filter: hue-rotate(180deg); }}
        75% {{ box-shadow: 0 0 32px #00c6ff, 0 0 12px #ffd200; filter: hue-rotate(270deg); }}
        100% {{ box-shadow: 0 0 24px #ffd200, 0 0 0px #00c6ff; filter: hue-rotate(360deg); }}
    }}
    .colorful-animated-logo {{
        animation: colorfulGlow 2.5s linear infinite;
        transition: box-shadow 0.3s, filter 0.3s;
    }}
    </style>
    <div class='sidebar-logo' style='margin-top:0;'>
        <img class='colorful-animated-logo' src='data:image/png;base64,{encoded_logo}' alt='Logo' style='width:150px;height:150px;border-radius:30%;box-shadow:0 2px 12px #00c6ff;border:2px solid #ffd200;margin-bottom:8px;background:#232526;object-fit:cover;'>
        <span style='color:#00c6ff;font-size:1.1em;font-family:sans-serif;font-weight:bold;text-shadow:0 1px 6px #ffd200;'></span>
    </div>
    """,
    unsafe_allow_html=True
)


# Animated title and caption

# Animated title and caption with vibrant colors

st.markdown(
    """
    <style>
    @keyframes neonBounce {
        0% { transform: scale(0.95) translateY(-30px); opacity: 0.2; }
        40% { transform: scale(1.05) translateY(10px); opacity: 1; }
        60% { transform: scale(1.02) translateY(-5px); }
        80% { transform: scale(1.01) translateY(0px); }
        100% { transform: scale(1) translateY(0px); }
    }
    .neon-title {
        text-align: center;
        font-size: 3em;
        font-family: 'Orbitron', 'monospace';
        font-weight: bold;
        letter-spacing: 2px;
        color: #00ffea;
        background: linear-gradient(90deg, #00ffea, #ff00c8, #ffea00, #00ffea);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        background-clip: text;
        animation: neonBounce 1.8s cubic-bezier(.68,-0.55,.27,1.55) 1, neonGlow 2.5s linear infinite alternate;
        text-shadow:
            0 0 12px #00ffea,
            0 0 24px #ff00c8,
            0 0 36px #ffea00,
            0 0 48px #00ffea,
            0 0 60px #ff00c8;
        /* Remove text-fill-color: transparent for visibility */
    }
    @keyframes neonGlow {
        0% { text-shadow: 0 0 12px #00ffea, 0 0 24px #ff00c8, 0 0 36px #ffea00; }
        50% { text-shadow: 0 0 36px #ffea00, 0 0 48px #00ffea, 0 0 60px #ff00c8; }
        100% { text-shadow: 0 0 12px #ff00c8, 0 0 24px #00ffea, 0 0 36px #ffea00; }
    }
    .neon-desc {
        text-align: center;
        font-size: 1.3em;
        font-family: 'Montserrat', 'sans-serif';
        color: #ff00c8;
        text-shadow: 0 0 12px #00ffea, 0 0 24px #ffea00;
        margin-bottom: 0.5em;
        animation: neonBounce 2.2s cubic-bezier(.68,-0.55,.27,1.55) 1;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Montserrat:wght@500&display=swap" rel="stylesheet">
    <h1 class='neon-title'>🗞️ Journalist Agent <span style="color:#ffea00;">NewsCraft.AI</span> 🤖</h1>
    <p class='neon-desc'>Generate High-quality articles with <span style="color:#00ffea;">Journalist Agent NewsCraft.AI</span> by researching, writing and editing quality articles on autopilot.</p>
    """,
    unsafe_allow_html=True
)

openai_api_key = st.text_input("Enter OpenAI API Key for GPT-4.1-nano (lower cost)", type="password")
serp_api_key = st.text_input("Enter Serp API Key for Search functionality", type="password")


# Article customization options
st.subheader("Customize Your Article")
length = st.selectbox("Article Length", ["Short (5 paragraphs)", "Medium (10 paragraphs)", "Long (15+ paragraphs)"])
style = st.selectbox("Writing Style", ["Formal", "Casual", "Analytical", "Storytelling"])
tone = st.selectbox("Tone", ["Neutral", "Positive", "Negative", "Balanced"])
audience = st.selectbox("Target Audience", ["General", "Students", "Professionals", "Researchers"])
language = st.selectbox("Language", ["English", "Hindi", "French", "Spanish", "German"])

# Source filtering options
st.subheader("Source Filtering")
preferred_domains = st.multiselect(
    "Preferred Source Domains (optional)",
    [".gov", ".edu", ".org", "nytimes.com", "bbc.com", "reuters.com", "indiatoday.in", "thehindu.com"]
)

if openai_api_key and serp_api_key:
    searcher = Agent(
        name="Searcher",
        role="Searches for top URLs based on a topic",
        model=OpenAIChat(id="gpt-4.1-nano", api_key=openai_api_key, temperature=0.2, max_tokens=500),
        description=dedent(
            """\
        You are a world-class journalist for the New York Times. Given a topic, generate a list of 3 search terms
        for writing an article on that topic. Then search the web for each term, analyse the results
        and return the 10 most relevant URLs. If the user has specified preferred domains, prioritize those sources.
        """
        ),
        instructions=[
            "Given a topic, first generate a list of 3 search terms related to that topic.",
            "For each search term, `search_google` and analyze the results.",
            "If the user has specified preferred domains, prioritize URLs from those domains.",
            "From the results of all searches, return the 10 most relevant URLs to the topic.",
            "Remember: you are writing for the New York Times, so the quality of the sources is important.",
        ],
        tools=[SerpApiTools(api_key=serp_api_key)],
        add_datetime_to_instructions=True,
    )
    writer = Agent(
        name="Writer",
        role="Retrieves text from URLs and writes a high-quality article",
        model=OpenAIChat(id="gpt-4.1-nano", api_key=openai_api_key, temperature=0.2, max_tokens=500),
        description=dedent(
            """\
        You are a senior writer for the New York Times. Given a topic and a list of URLs,
        your goal is to write a high-quality NYT-worthy article on the topic.
        """
        ),
        instructions=[
            "Given a topic and a list of URLs, first read the article using `get_article_text`.",
            f"Then write a high-quality NYT-worthy article on the topic. The article should be well-structured, informative, and engaging. Style: {style}. Tone: {tone}. Audience: {audience}.",
            f"Ensure the length matches the user's choice: {length}.",
            "Ensure you provide a nuanced and balanced opinion, quoting facts where possible.",
            "Remember: you are writing for the New York Times, so the quality of the article is important.",
            "Focus on clarity, coherence, and overall quality.",
            "Never make up facts or plagiarize. Always provide proper attribution.",
        ],
        tools=[Newspaper4kTools()],
        add_datetime_to_instructions=True,
        markdown=True,
    )

    editor = Agent(
        name="Editor",
        model=OpenAIChat(id="gpt-4.1-nano", api_key=openai_api_key, temperature=0.2, max_tokens=500),
        team=[searcher, writer],
        description="You are a senior NYT editor. Given a topic, your goal is to write a NYT worthy article.",
        instructions=[
            "Given a topic and article customization options, ask the search journalist to search for the most relevant URLs for that topic, prioritizing preferred domains if specified.",
            "Show the user the list of found URLs and let them select which ones to use for the article.",
            "Then pass a description of the topic, selected URLs, and customization options to the writer to get a draft of the article.",
            "Edit, proofread, and refine the article to ensure it meets the high standards of the New York Times.",
            "The article should be extremely articulate and well written. Focus on clarity, coherence, and overall quality.",
            "Ensure the article is engaging and informative.",
            "Remember: you are the final gatekeeper before the article is published.",
        ],
        add_datetime_to_instructions=True,
        markdown=True,
    )

    query = st.text_input("What do you want the AI journalist to write an Article on?")

    # Placeholder for URLs found by the searcher
    found_urls = []

    if query:
        # Indented block for 'if query:'
        with st.spinner("Searching for sources..."):
            try:
                searcher_response = searcher.run({
                    "topic": query,
                    "preferred_domains": preferred_domains
                }, stream=False)
                st.write("Searcher raw response:", searcher_response)  # Debug output
                found_urls = []
                if hasattr(searcher_response, "content"):
                    if isinstance(searcher_response.content, list):
                        found_urls = searcher_response.content
                    elif isinstance(searcher_response.content, str):
                        import re
                        # Extract URLs from markdown links: [Title](URL)
                        md_links = re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)', searcher_response.content)
                        if md_links:
                            # Use the title and URL for display
                            found_urls = [f"{title} ({url})" for title, url in md_links]
                        else:
                            # Fallback: extract plain URLs
                            found_urls = re.findall(r'https?://\S+', searcher_response.content)
                if not found_urls:
                    st.error("No sources found. Please check your SerpApi key, your topic, or try again later.")
            except Exception as e:
                st.error(f"Error during search: {e}")
                found_urls = []

        if found_urls:
            st.subheader("Select Sources for Your Article")
            # Extract just the URL part for selection and agent input
            import re
            url_choices = []
            url_map = {}
            for item in found_urls:
                match = re.match(r"(.+?) \((https?://[^)]+)\)", item)
                if match:
                    title, url = match.groups()
                    url_choices.append(f"{title}")
                    url_map[title] = url
                else:
                    url_choices.append(item)
                    url_map[item] = item
            selected_titles = st.multiselect("Choose URLs to use:", url_choices)
            selected_urls = [url_map[t] for t in selected_titles]
            generate_btn = st.button("Generate Article")
            article = ""
            if selected_urls and generate_btn:
                with st.spinner("Writing your customized article..."):
                    try:
                        response = editor.run({
                            "topic": query,
                            "selected_urls": selected_urls,
                            "length": length,
                            "style": style,
                            "tone": tone,
                            "audience": audience,
                            "language": language
                        }, stream=False)
                        st.write("Editor raw response:", response)  # Debug output
                        article = response.content if hasattr(response, "content") else str(response)
                        st.write(article)
                    except Exception as e:
                        st.error(f"Error during article generation: {e}\nMake sure you select valid sources (URLs) only.")
                        article = ""

                    # Generate summary and key points (simple split for demo)
                    st.subheader("Summary & Key Points")
                    if article:
                        summary = article[:500] + "..." if len(article) > 500 else article
                        st.write("**Summary:**", summary)
                        import re
                        key_points = re.split(r'(?<=[.!?]) +', article)[:5]
                        st.write("**Key Points:**")
                        for i, point in enumerate(key_points, 1):
                            st.markdown(f"{i}. {point}")

                    # Download options
                    st.subheader("Download & Share")
                    st.download_button("Download Article (Markdown)", article, file_name="article.md")
                    st.download_button("Download Summary (Text)", summary, file_name="summary.txt")
                    st.info("For PDF/DOCX download, integrate with 'pdfkit' or 'python-docx'.")

                    # Share options (demo)
                    st.write("Share your article:")
                    st.markdown("[Share via Email](mailto:?subject=AI%20Journalist%20Article&body=See%20attached%20article)")
                    st.markdown("[Share on Twitter](https://twitter.com/intent/tweet?text=Check%20out%20this%20AI-generated%20article!)")

                    # User feedback & rating
                    st.subheader("Rate & Feedback")
                    rating = st.slider("Rate this article:", 1, 5, 3)
                    feedback = st.text_area("Your feedback:")
                    if st.button("Submit Feedback"):
                        st.success("Thank you for your feedback!")

                    # History & Saved Articles (simple session state)
                    if "history" not in st.session_state:
                        st.session_state["history"] = []
                    st.session_state["history"].append({
                        "query": query,
                        "article": article,
                        "summary": summary,
                        "rating": rating,
                        "feedback": feedback
                    })
                    st.markdown('<div class="history-section">', unsafe_allow_html=True)
                    st.subheader("History & Saved Articles")
                    for idx, item in enumerate(st.session_state["history"][::-1], 1):
                        st.markdown(f"**{idx}. Query:** <span style='color:#ffd200'>{item['query']}</span>", unsafe_allow_html=True)
                        st.markdown(f"**Summary:** <span style='color:#00c6ff'>{item['summary']}</span>", unsafe_allow_html=True)
                        st.markdown(f"**Rating:** <span style='color:#f7971e'>{item['rating']}</span>", unsafe_allow_html=True)
                        if st.button(f"Show Full Article {idx}"):
                            st.markdown(f"<div style='background:linear-gradient(90deg,#232526,#2c5364);color:#f8fafc;padding:16px;border-radius:12px;box-shadow:0 2px 12px #00c6ff;'>"+item["article"]+"</div>", unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)