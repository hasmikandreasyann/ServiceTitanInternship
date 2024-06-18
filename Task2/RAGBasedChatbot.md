# RAG-Based Chatbot for PDF

This project aims to create a chatbot that allows users to interact with PDF installation manuals for various home equipment, such as air conditioners, sinks, and water heaters. We will use a Retrieval-Augmented Generation (RAG) system to achieve this. A RAG system enhances a generative model with a retrieval mechanism that can fetch relevant information from a large corpus of documents, ensuring accurate and contextually appropriate responses. Below, I will detail each component of the RAG system, describing the choices for tools and methodologies to be employed.

## Component of the RAG system (embedder, PDF processor, vector DB, LLM response generation, etc.). 
### PDF Processor:
 The PDF processor extracts text and metadata from PDF files. This extracted information is then used to build a searchable corpus and generate embeddings. We can choose PyMuPDF. It is a high-performance Python library for data extraction, analysis, conversion & manipulation of PDF documents. This library is lightweight, efficient, and capable of handling various PDF complexities, such as embedded images and text encodings. It allows for precise text extraction, crucial for creating accurate embeddings and a searchable database.
We can also use PyPDF2 or PDFMiner; however, based on my research, they are relatively slower and more complex to implement than PyMuPDF. Adobe PDF SDK is highly reliable but expensive.

### Embedder: 
The embedder converts textual information into high-dimensional vectors, which can be efficiently searched and compared. We can choose OpenAI Embeddings. They are well-suited for capturing semantic information. They convert text into numerical vectors, enabling efficient similarity comparison, search, and retrieval of relevant information. They have lower computational requirements that make them scalable for handling multiple PDFs and user interactions simultaneously. This improves the chatbot's ability to understand and respond to queries accurately. Also, embeddings handle large datasets quite well, enhancing the overall performance and capability of the chatbot. These embeddings are robust and trained on diverse datasets, ensuring they can handle the varied language found in installation manuals. There are some suitable models, such as Ada and Babbage. For example, we can use the text-embedding-ada-002 model. It offers high-quality embeddings that capture semantic information effectively.
We should avoid using GloVe or Word2Vec. These models are less suited for capturing the nuanced meanings in sentences than transformer-based models like those from OpenAI or SBERT. Both of these produce static word embeddings. This means that each word has a single representation, regardless of its context within a sentence. For example, the word "apple" would have the same embedding whether it appears in " Apple Store" or "green apple."
Additionally, the semantic similarity captured by GloVe and Word2Vec is limited by their inability to account for context. This can result in less accurate retrieval of relevant document sections, as they might not fully understand the nuanced queries users might pose about specific installation steps or troubleshooting procedures. They are relatively outdated and have fewer capabilities than new ones.

### Vector Database:
 A vector database stores pieces of information as vectors. Vector databases cluster related items together, enabling similarity searches and the construction of powerful AI models. Here, I can choose Pinecone. One of the reasons is that it is efficient for storing and querying high-dimensional vectors as I am using text-embedding-ada-002, which produces complex and high-dimensional representations of text. Pinecone is suitable. It is also fast. It uses ANN search algorithms and can quickly retrieve vectors that are most similar to a given query.  It allows for seamless scaling as the volume of data and queries increases. It supports automatic scaling and can handle large-scale deployments without compromising search performance or reliability.
LLM for Response Generation: The LLM generates responses based on the retrieved information from the vector database, ensuring the output is coherent and contextually appropriate. Once again, I will use OpenAI here. OpenAI GPT-4: This is one of the most advanced and popular language models. It can generate human-like text and understand complex queries. This capability is important for accurately interpreting user queries related to installation procedures and providing contextually appropriate responses. So it can provide users with clear and understandable explanations, instructions, or troubleshooting guidance, as found in installation manuals. One of the advantages of GPT-4 is that it can be fine-tuned on domain-specific data, such as installation manuals or related technical documents. Fine-tuning helps adapt the model's responses to the specific language and terminology used in the manuals, improving accuracy and relevance. It is also compatible with my chosen OpenAI embedding. Regarding alternative considerations, I used different chatbots that used other models like BERT or XLNet, which were not too impressive. Hugging Face Transformers library offers a range of pre-trained models that can be fine-tuned. Still, it requires more effort to achieve the same performance and ease of integration level as OpenAI's models.

## Challenges 
One challenge I can think of is the high dimensionality of the embeddings. My chosen model, text-embedding-ada-002, has a high-dimensional vector representation, which can be resource-intensive to store and query efficiently, especially when dealing with a large corpus of installation manuals. A solution for that can be using dimensionality reduction techniques such as PCA or SVD (most likely PCA). They reduce the dimensionality of embeddings while preserving their semantic information, which can help optimize storage space and improve query performance without significantly compromising accuracy. Additionally, as I mentioned, using a vector database, Pinecone, optimized for high-dimensional vectors, can help solve some of the challenges related to storage and retrieval efficiency.

Another problem can be the domain-specific language. Installation manuals often contain specialized technical terms that are most likely not well-represented in general language models. This can lead to inaccuracies or misunderstandings in the embeddings and subsequently affect the chatbot's ability to retrieve and generate accurate responses. A solution to that is to fine-tune the embeddings on a domain-specific corpus or perform additional preprocessing steps tailored to the language found in installation manuals. Fine-tuning involves retraining the embeddings on a dataset that includes explicitly installation manuals or similar technical documents, which can help the embeddings capture the domain-specific language better and improve the accuracy of retrieval and response generation. Also, using domain-specific dictionaries might enhance the model's model's understanding of technical terms and their context.

Another challenge is understanding diagrams or graphics in PDF installation manuals. Diagrams and graphics often include information visually that may not be explicitly described in the text, such as component interactions and step-by-step procedures that are crucial for installation and troubleshooting. This can be solved by using Image Recognition Tools. These tools can extract relevant information from visuals and convert it into textual descriptions or structured data that the chatbot can interpret and use to generate responses. For example, we can use Google Cloud Vision API or Microsoft Azure Computer Vision API. They both provide robust image recognition capabilities, detecting objects' text within images. It can generate descriptive metadata that helps understand the content of diagrams and graphics. We can also build our deep learning models using frameworks such as TensorFlow or PyTorch for image recognition and description. 
 
## Questions
### Answerable 
    1. "How do I adjust the thermostat settings on my AC unit to optimize energy efficiency during different seasons?"
The chatbot can retrieve relevant sections from the AC installation manual, analyze the instructions, and provide specific advice based on the extracted information.

    2. "What are the environmental requirements for installing an outdoor air conditioning unit?"
It can locate and summarize the environmental requirements section from the air conditioning unit's installation manual.

    3. "How do I calibrate the temperature sensor on my water heater?"
The chatbot can find the calibration instructions in the water heater manual and explain the procedure step by step.

    4. "How do I troubleshoot error code E1 on my air conditioner?"
The chatbot can retrieve the troubleshooting section from the air conditioner manual explicitly addressing error codes and their resolutions.

    5. "Can you explain the wiring diagram for connecting my new thermostat to the HVAC system?"
The chatbot can reference the wiring diagram section of the thermostat installation manual and provide step-by-step instructions and diagram references.

### Might fail to answer
    1. "How can I reduce noise from my air conditioner during operation?"
Noise reduction techniques may involve specific modifications or aftermarket solutions not covered in basic installation manuals.

    2. "Why the battery is not working on my AC remote controller?"
The chatbot can not guess it, as most likely the reason is not mentioned in installation manuals.

    3. " Can you recommend a better AC model than the one I bought?"
The chatbot is limited to information within the manuals and cannot provide comparisons with other models or brands.

    4. "How much will it cost to hire a professional to install a new air conditioner?"
The chatbot is limited to information within the manuals, and service pricing information is most likely not included in installation manuals.

    5. "What is the average lifespan of a water heater?"
Again, the chatbot is limited to information within the manuals, and lifespan information can vary based on usage, maintenance, and other factors that are not typically detailed in manuals.
