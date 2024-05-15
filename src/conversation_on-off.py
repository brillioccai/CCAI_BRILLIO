import *

def create_conversation_pipeline(Project_id, conv_id, ha_id, eu_id, human_agent_text, end_user_text, conversation_flag=False):
    ac_text_ha = analyze_content_text.analyze_content_text(Project_id, conv_id, ha_id, human_agent_text)
    ac_text_eu = analyze_content_text.analyze_content_text(Project_id, conv_id, eu_id, end_user_text)
    if conversation_flag:
        complete_conversation(Project_id, conv_id)