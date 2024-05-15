def create_knowledge_base(project_id, display_name):
    """Creates a Knowledge base.

    Args:
        project_id: The GCP project linked with the agent.
        display_name: The display name of the Knowledge base."""
    from google.cloud import dialogflow_v2beta1 as dialogflow

    client = dialogflow.KnowledgeBasesClient()
    project_path = client.common_project_path(project_id)

    knowledge_base = dialogflow.KnowledgeBase(display_name=display_name)

    response = client.create_knowledge_base(
        parent=project_path, knowledge_base=knowledge_base
    )

    print("Knowledge Base created:\n")
    print("Display Name: {}\n".format(response.display_name))
    print("Name: {}\n".format(response.name))
    return response.name.split("/")[-1]