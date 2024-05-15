import *

def create_pipeline(Project_id, Knowledge_base_name, Document_name, Conversation_profile_name):
    kb_id = create_knowledge_base.create_knowledge_base(Project_id, Knowledge_base_name)
    print(kb_id)
    doc_id = create_document.create_document(Project_id, kb_id,Document_name,"text/csv","FAQ","gs://faq_buck/FAQ_Folder/FAQ_assist_final_utf8.csv") 
    print(doc_id)
    cp_id = create_conversation_profile.create_conversation_profile_article_faq(Project_id, Conversation_profile_name, kb_id, kb_id)
    print(cp_id)
    conv_id = create_conversation.create_conversation(Project_id, cp_id)
    print(conv_id)
    eu_id = create_participant.create_participant(Project_id, conv_id, dialogflow.Participant.Role.END_USER)
    print(eu_id)
    ha_id = create_participant.create_participant(Project_id, conv_id, dialogflow.Participant.Role.HUMAN_AGENT)
    print(ha_id)
    return conv_id, ha_id, eu_id