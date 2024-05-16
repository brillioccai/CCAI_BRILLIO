# CCAI_BRILLIO

**FAQ_ASSIST IN CCAI**

**OVERVIEW**

This project, named "brldi-ds-capabilities-ccai" , utilizes the Dialogflow API to implement a FAQ_ASSIST system. Dialogflow is a natural language understanding platform that makes it easy to design and integrate conversational user interfaces into mobile apps, web applications, devices, bots, and more. The FAQ_ASSIST system built within this project aims to streamline the process of answering frequently asked questions (FAQs) by providing a conversational interface that can understand and respond to user queries in a natural language format.

**Create knowedge base**

In the initial phase of the project, we leveraged the Dialogflow API (v2beta1) to develop a comprehensive knowledge base. Through this process, we meticulously curated and organized a repository of frequently asked questions (FAQs) and their corresponding answers. By harnessing the capabilities of Dialogflow v2beta1, we ensured that our knowledge base system is equipped with advanced natural language understanding (NLU) functionalities, enabling seamless interaction and accurate retrieval of information for users

**Create FAQ dataset in CSV format**

Following the knowledge base creation, we uploaded a CSV file containing two columns - questions and their respective answers - to a Google Cloud Storage (GCS) bucket. This step facilitated the seamless integration of structured data into our knowledge base system, enhancing accessibility and efficiency in information retrieval for users.

**Create Conversation Profile**

Created a conversation profile, detailing the structure of user interactions. Subsequently, we integrated our FAQ dataset into this profile, establishing a knowledge base for efficient matching of user queries to relevant answers, thus enhancing the conversational system's effectiveness.

**Create Participant**

Created the "create_participant" function to define roles within our system, distinguishing between human agents and end users. This function streamlines the allocation of roles, facilitating seamless communication between agents and users in Agent Assist platform.

**Analyze content**

We created a function called "analyze_content_text," where an end-user's question is passed for analysis by the Dialogflow API. Subsequently, it returns the respective answer from the FAQ dataset.

**Nomenclature**

kb_id = knowledge base id

doc_id = document id

ha_id = human agent id

eu_id = end user id

cp_id = conversation profile id

conv_id = conversation id

ac_text_ha = analyze content text by human agent

ac_text_eu = analyze content text by end user
