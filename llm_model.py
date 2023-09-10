
from llama_index import VectorStoreIndex,download_loader, VectorStoreIndex, ServiceContext, StorageContext, load_index_from_storage
from pathlib import Path
from github import Github
import os
import shutil
import openai
import gradio as gr
import pypandoc

from pathlib import Path
from llama_index import download_loader

"""# Github Configeration"""

openai.api_key = os.environ.get("OPENAPI_API_KEY")

# username = 'Akhil-Sharma30'


"""# Reading the Files for LLM Model"""
class Llm_Training:
    def convert_to_markdown(input_file, output_file):
    
    # Converts a file to markdown format.

    # Args:
    # input_file (str): The path to the input file.
    # output_file (str): The path to the output markdown file.

    # Returns:
    # bool: True if conversion is successful, False otherwise.
    
        try:
            # Convert the input file to markdown format
            pypandoc.convert_file(input_file, 'markdown', outputfile=output_file)
            return True
        except Exception as e:
            print(f"Conversion error: {str(e)}")
            return False

    # Example usage:
    if __name__ == "__main__":
        input_file = "/content/covid_toy.csv"  # Replace with your input file path
        output_file = "output.md"  # Replace with your desired output file path

        if convert_to_markdown(input_file, output_file):
            print(f"File '{input_file}' converted to markdown successfully and saved as '{output_file}'.")
        else:
            print(f"Failed to convert '{input_file}' to markdown.")

    # Specify the path to the repository
    repo_dir = "/content/Akhil-Sharma30.github.io"

    # Check if the repository exists and delete it if it does
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)


    # def combine_md_files(folder_path):
    #     MarkdownReader = download_loader("MarkdownReader")
    #     loader = MarkdownReader()

    #     md_files = [file for file in folder_path.glob('*.md')]
    #     documents = None

    #     for file_path in md_files:
    #         document = loader.load_data(file=file_path)
    #         documents += document

    #     return documents

    # folder_path = Path('/content/Akhil-Sharma30.github.io/content')
    #combined_documents = combine_md_files(folder_path)

    # combined_documents will be a list containing the contents of all .md files in the folder
    def chatbot_function(query):
        openai.api_key = os.environ.get("OPENAPI_API_KEY")
        RemoteReader = download_loader("RemoteReader")

        loader = RemoteReader()

        document1 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/assets/README.md")
        document2 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/content/about.md")
        document3 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/content/cv.md")
        document4 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/content/post.md")
        document5 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/content/opensource.md")
        document6 = loader.load_data(url="https://raw.githubusercontent.com/Akhil-Sharma30/Akhil-Sharma30.github.io/main/content/supervised.md")

        data = document1+ document2 + document3+ document4 + document5+document6


        """# Vector Embedding"""

        index = VectorStoreIndex.from_documents(data)

        query_engine = index.as_query_engine()
        # response = query_engine.query("know akhil?")
        # print(response)

        response = query_engine.query(query)
        return response

    def Generative_response(prompt):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": ""
                }
            ],
            temperature=1,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return gpt_response.choices[0].message["content"]
