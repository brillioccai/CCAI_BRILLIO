def analyze_content_text(
    project_id: str, conversation_id: str, participant_id: str, text: str
):
    from google.cloud import dialogflow_v2beta1 as dialogflow

    """Analyze text message content from a participant.

    Args:
        project_id: The GCP project linked with the conversation profile.
        conversation_id: Id of the conversation.
        participant_id: Id of the participant.
        text: the text message that participant typed."""

    client = dialogflow.ParticipantsClient()
    participant_path = client.participant_path(
        project_id, conversation_id, participant_id
    )
    text_input = {"text": text, "language_code": "en-US"}
    response = client.analyze_content(
        participant=participant_path, text_input=text_input
    )
    print("AnalyzeContent Response:", response)
    print(f"Reply Text: {response.reply_text}")

    for suggestion_result in response.human_agent_suggestion_results:
        if suggestion_result.error is not None:
            print(f"Error: {suggestion_result.error.message}")
        if suggestion_result.suggest_articles_response:
            for answer in suggestion_result.suggest_articles_response.article_answers:
                print(f"Article Suggestion Answer: {answer.title}")
                print(f"Answer Record: {answer.answer_record}")
        if suggestion_result.suggest_faq_answers_response:
            for answer in suggestion_result.suggest_faq_answers_response.faq_answers:
                print(f"Faq Answer: {answer.answer}")
                print(f"Answer Record: {answer.answer_record}")
        if suggestion_result.suggest_smart_replies_response:
            for (
                answer
            ) in suggestion_result.suggest_smart_replies_response.smart_reply_answers:
                print(f"Smart Reply: {answer.reply}")
                print(f"Answer Record: {answer.answer_record}")

    for suggestion_result in response.end_user_suggestion_results:
        if suggestion_result.error:
            print(f"Error: {suggestion_result.error.message}")
        if suggestion_result.suggest_articles_response:
            for answer in suggestion_result.suggest_articles_response.article_answers:
                print(f"Article Suggestion Answer: {answer.title}")
                print(f"Answer Record: {answer.answer_record}")
        if suggestion_result.suggest_faq_answers_response:
            for answer in suggestion_result.suggest_faq_answers_response.faq_answers:
                print(f"Faq Answer: {answer.answer}")
                print(f"Answer Record: {answer.answer_record}")
        if suggestion_result.suggest_smart_replies_response:
            for (
                answer
            ) in suggestion_result.suggest_smart_replies_response.smart_reply_answers:
                print(f"Smart Reply: {answer.reply}")
                print(f"Answer Record: {answer.answer_record}")

    return response