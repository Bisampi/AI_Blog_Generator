import os
from secret_api_key import huggingface_api_key
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
import streamlit as st

# Set token as environment variable
os.environ['HUGGINGFACEHUB_API_TOKEN'] = huggingface_api_key

# LLM Setup
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=500,
    token=huggingface_api_key,
)

# Templates
template_for_title_suggestion = PromptTemplate(
    input_variables=['topic'],
    template='''
Generate a detailed blog post on the topic: "{topic}".
Give any ten most specific attention-grabbing titles for the blog post.
Just give the titles, no explanation.
'''
)

template_for_blog_content = PromptTemplate(
    input_variables=['title', 'tone', 'audience', 'keywords', 'blog_length'],
    template='''
Write a blog post titled: "{title}".
The tone should be "{tone}" and the target audience is "{audience}".
Include these keywords: "{keywords}".
The blog post should be approximately {blog_length} words long.
Write a compelling and informative blog post.
'''
)

# Streamlit UI
st.title("📝 AI Blog Generator")

# 1. Topic input section
topic_name = st.text_input("Enter blog topic:")
if st.button("Submit Topic"):
    st.session_state['topic_name'] = topic_name
    title_response = template_for_title_suggestion | llm
    titles = title_response.invoke({'topic': topic_name}).split('\n')
    st.session_state['titles'] = [t.strip() for t in titles if t.strip()]
    st.session_state['step'] = 'titles'

# 2. Title selection section
if st.session_state.get('step') == 'titles':
    selected_title = st.selectbox("Select one of the generated blog titles:", st.session_state['titles'])
    if st.button("Continue to Blog Form"):
        st.session_state['selected_title'] = selected_title
        st.session_state['step'] = 'form'

# 3. Blog form input section
if st.session_state.get('step') == 'form':
    st.subheader(f"Blog Generator for: {st.session_state['selected_title']}")

    tone = st.text_input("Enter blog tone:", key="tone_input")
    audience = st.text_input("Enter target audience:", key="audience_input")
    blog_length = st.number_input("Blog length (words)", min_value=100, value=300)
    keywords = st.text_input("Enter keywords separated by commas:")

    if st.button("Generate Blog"):
        blog_prompt = template_for_blog_content.format(
            title=st.session_state['selected_title'],
            tone=tone,
            audience=audience,
            keywords=keywords,
            blog_length=blog_length
        )
        blog_output = llm.invoke(blog_prompt)
        st.session_state['generated_blog'] = blog_output
        st.session_state['step'] = 'done'

# 4. Display blog output
if st.session_state.get('step') == 'done':
    st.subheader("📝 Generated Blog")
    st.write(st.session_state['generated_blog'])
