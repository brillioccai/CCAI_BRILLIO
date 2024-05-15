def create_conversation_profile_article_faq(
    project_id,
    display_name,
    article_suggestion_knowledge_base_id=None,
    faq_knowledge_base_id=None,
):
    """Creates a conversation profile with given values

    Args: project_id:  The GCP project linked with the conversation profile.
        display_name: The display name for the conversation profile to be
        created.
        article_suggestion_knowledge_base_id: knowledge base id for article
        suggestion.
        faq_knowledge_base_id: knowledge base id for faq."""

    client = dialogflow.ConversationProfilesClient()
    project_path = client.common_project_path(project_id)

    conversation_profile = {
        "display_name": display_name,
        "human_agent_assistant_config": {
            "human_agent_suggestion_config": {"feature_configs": []}
        },
        "language_code": "en-US",
    }

    if article_suggestion_knowledge_base_id is not None:
        as_kb_path = dialogflow.KnowledgeBasesClient.knowledge_base_path(
            project_id, article_suggestion_knowledge_base_id
        )
        feature_config = {
            "suggestion_feature": {"type_": "ARTICLE_SUGGESTION"},
            "suggestion_trigger_settings": {
                "no_small_talk": True,
                "only_end_user": True,
            },
            "query_config": {
                "knowledge_base_query_source": {"knowledge_bases": [as_kb_path]},
                "max_results": 3,
            },
        }
        conversation_profile["human_agent_assistant_config"][
            "human_agent_suggestion_config"
        ]["feature_configs"].append(feature_config)
    if faq_knowledge_base_id is not None:
        faq_kb_path = dialogflow.KnowledgeBasesClient.knowledge_base_path(
            project_id, faq_knowledge_base_id
        )
        feature_config = {
            "suggestion_feature": {"type_": "FAQ"},
            "suggestion_trigger_settings": {
                "no_small_talk": True,
                "only_end_user": True,
            },
            "query_config": {
                "knowledge_base_query_source": {"knowledge_bases": [faq_kb_path]},
                "max_results": 3,
            },
        }
        conversation_profile["human_agent_assistant_config"][
            "human_agent_suggestion_config"
        ]["feature_configs"].append(feature_config)

    response = client.create_conversation_profile(
        parent=project_path, conversation_profile=conversation_profile
    )

    print("Conversation Profile created:")
    print("Display Name: {}".format(response.display_name))
    # Put Name is the last to make it easier to retrieve.
    print("Name: {}".format(response.name))
    return response.name.split("/")[-1]