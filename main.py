from src import *

conv_id, ha_id, eu_id = create_conversation_pipeline.create_pipeline("brldi-ds-capabilities-ccai", "FAQ_KB_NEW_3", "FAQ_ASSIST_NEW_3", "CONV_PROFILE_NEW_3")

conversation_on-off.create_conversation_pipeline("brldi-ds-capabilities-ccai", conv_id, ha_id, eu_id, "My credit card payment is declined", "")