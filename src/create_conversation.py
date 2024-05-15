def create_conversation(project_id, conversation_profile_id):
    """Creates a conversation with given values

    Args:
        project_id:  The GCP project linked with the conversation.
        conversation_profile_id: The conversation profile id used to create
        conversation."""

    client = dialogflow.ConversationsClient()
    conversation_profile_client = dialogflow.ConversationProfilesClient()
    project_path = client.common_project_path(project_id)
    conversation_profile_path = conversation_profile_client.conversation_profile_path(
        project_id, conversation_profile_id
    )
    conversation = {"conversation_profile": conversation_profile_path}
    response = client.create_conversation(
        parent=project_path, conversation=conversation
    )

    print("Life Cycle State: {}".format(response.lifecycle_state))
    print("Conversation Profile Name: {}".format(response.conversation_profile))
    print("Name: {}".format(response.name))
    return response.name.split("/")[-1]