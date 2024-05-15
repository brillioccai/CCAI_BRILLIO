def create_participant(project_id: str, conversation_id: str, role: str):
    from google.cloud import dialogflow_v2beta1 as dialogflow

    """Creates a participant in a given conversation.

    Args:
        project_id: The GCP project linked with the conversation profile.
        conversation_id: Id of the conversation.
        participant: participant to be created."""

    client = dialogflow.ParticipantsClient()
    conversation_path = dialogflow.ConversationsClient.conversation_path(
        project_id, conversation_id
    )
    # if role in ROLES:
    response = client.create_participant(
        parent=conversation_path, participant={"role": role}, timeout=600
    )
    print("Participant Created.",response)
    print(f"Role: {response.role}")
    print(f"Name: {response.name}")

    return response.name.split("/")[-1]