def complete_conversation(project_id, conversation_id):
    """Completes the specified conversation. Finished conversations are purged from the database after 30 days.

    Args:
        project_id: The GCP project linked with the conversation.
        conversation_id: Id of the conversation."""

    client = dialogflow.ConversationsClient()
    conversation_path = client.conversation_path(project_id, conversation_id)
    conversation = client.complete_conversation(name=conversation_path)
    print("Completed Conversation.")
    print("Life Cycle State: {}".format(conversation.lifecycle_state))
    print("Conversation Profile Name: {}".format(conversation.conversation_profile))
    print("Name: {}".format(conversation.name))
    return conversation