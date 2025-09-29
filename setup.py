from setuptools import setup, find_packages

setup(
    name="ai-health-chatbot",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Ahiachi Wondikom",
    author_email="wondikomm@gmail.com",
    description="AI-powered health chatbot using LangChain, Pinecone, OpenAI, and Flask.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Miss-Marvis/ai-health-chatbot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
