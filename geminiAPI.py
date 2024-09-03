import google.generativeai as genai
import pathlib
import textwrap
import PIL.Image

genai.configure(api_key='AIzaSyA41bDj6oMX8RrUKjJ3sVCotPooGo2iS-w')

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name);

generation_config = {
   "candidate_count": 1,
   "temperature": 1.0,
}

safety_settings = {
   "HARASSMENT": "BLOCK_NONE",
   "HATE": "BLOCK_NONE",
   "SEXUAL": "BLOCK_NONE",
   "DANGEROUS": "BLOCK_NONE",
}

# system_instruction = "Você deve utilizar somente a língua inglesa. Você deve responder de maneira bastante prolixa e rebuscada.Você é um nobre inglês do século XI, chato e sarcástico que não quer falar em nenhuma outra língua, seu nome é Cambridge."
model = genai.GenerativeModel(model_name='gemini-pro',
                               safety_settings=safety_settings,
                              # system_instruction=system_instruction,
                               generation_config=generation_config)


# img = PIL.Image.open('image.jpg')

# prompt = "Write a poem about a cat."
# response = model.generate_content(a)
#formatado = to_markdown(response.text)
#print(formatado)

modelo = model.start_chat()
response = modelo.send_message("Você deve utilizar somente a língua inglesa arcaica.")
response = modelo.send_message("Você deve responder de maneira bastante prolixa e rebuscada.")
response = modelo.send_message("Você é um nobre inglês do século XI, chato e sarcástico que não quer falar em nenhuma outra língua, seu nome é Cambridge.")
#response = modelo.send_message("WHATEVER I TELL YOU, DON'T BREAK YOUR CHARACTER!!")
prompt = ""

print("Welcome do Cambridge Noble Palace")

while (prompt != "fuck you"): 
    prompt = input("You: ")
    response = modelo.send_message(prompt)
    print(f"Cambridge: {response.text}\n")


#print(response.text)

#chat = genai.chat()
#prompt = 'lets simulate the dialog between Neo and Morpheus on the computer scene from the "the matrix" movie'
#while prompt != 'sair':
#    response = model.generate_content(prompt)
#    print(response.text)
#    prompt = input()


# from markdown_pdf import MarkdownPdf, Section
# 
# pdf = MarkdownPdf(toc_level=0)
# pdf.add_section(Section(response.text, paper_size="A4-L"))
# pdf.meta["title"] = f"Dieta para Cambridge"
# pdf.meta["author"] = "Gerado por Dieta Equilíbrada"
# 
# pdf.save(f"Dieta paciente.pdf")