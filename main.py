from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
load_dotenv()

def main():
    print("Hello from langu!")
    information = """Ibn Rushd[a] (14 April 1126 – 11 December 1198), Latinized as Averroes,[b] was an Andalusian polymath and jurist who was proficient in a variety of intellectual fields, including philosophy, theology, medicine, astronomy, physics, psychology, mathematics, neurology, Islamic jurisprudence, law, and linguistics. The author of more than 100 books and treatises,[1][2] his philosophical works include numerous commentaries on Aristotle, for which he was known in the Western world as "The Commentator" and "Father of Rationalism".

Averroes was a strong proponent of Aristotelianism; he attempted to restore what he considered the original teachings of Aristotle and opposed the Neoplatonist tendencies of earlier Muslim thinkers, such as al-Farabi and Avicenna. He also defended the pursuit of philosophy against criticism by Ash'ari theologians such as Al-Ghazali. Averroes argued that philosophy was permissible in Islam and even compulsory among certain elites. He also argued scriptural text should be interpreted allegorically if it appeared to contradict conclusions reached by reason and philosophy. In Islamic jurisprudence, he wrote the Bidāyat al-Mujtahid on the differences between Islamic schools of law and the principles that caused their differences. In medicine, he proposed a new theory of stroke, described the signs and symptoms of Parkinson's disease for the first time, and might have been the first to identify the retina as the part of the eye responsible for sensing light. His medical book Al-Kulliyat fi al-Tibb, translated into Latin and known as the Colliget, became a textbook in Europe for centuries"""

    summary_template = """
    given the information {information} about the person i want you to create:
    1. short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    # llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0)
    llm = ChatOllama(model = "llama3.1:8b", temperature = 0, base_url="http://localhost:11434")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)



if __name__ == "__main__":
    main()
