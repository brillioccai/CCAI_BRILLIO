def create_document(
    project_id, knowledge_base_id, display_name, mime_type, knowledge_type, content_uri
):
    """Creates a Document.

    Args:
        project_id: The GCP project linked with the agent.
        knowledge_base_id: Id of the Knowledge base.
        display_name: The display name of the Document.
        mime_type: The mime_type of the Document. e.g. text/csv, text/html,
            text/plain, text/pdf etc.
        knowledge_type: The Knowledge type of the Document. e.g. FAQ,
            EXTRACTIVE_QA.
        content_uri: Uri of the document, e.g. gs://path/mydoc.csv,
            http://mypage.com/faq.html."""
    from google.cloud import dialogflow_v2beta1 as dialogflow

    client = dialogflow.DocumentsClient()
    knowledge_base_path = dialogflow.KnowledgeBasesClient.knowledge_base_path(
        project_id, knowledge_base_id
    )

    document = dialogflow.Document(
        display_name=display_name, mime_type=mime_type, content_uri=content_uri
    )

    document.knowledge_types.append(
        getattr(dialogflow.Document.KnowledgeType, knowledge_type)
    )

    response = client.create_document(parent=knowledge_base_path, document=document)
    print("Waiting for results...")
    document = response.result(timeout=120)
    print("Created Document:")
    print(" - Display Name: {}".format(document.display_name))
    print(" - Knowledge ID: {}".format(document.name))
    print(" - MIME Type: {}".format(document.mime_type))
    print(" - Knowledge Types:")
    for knowledge_type in document.knowledge_types:
        print("    - {}".format(knowledge_type))
    print(" - Source: {}\n".format(document.content_uri))
    return document.name.split("/")[-1]