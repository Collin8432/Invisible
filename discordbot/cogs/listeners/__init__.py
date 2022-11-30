from .on_connect import *
from .on_disconnect import *
from .on_error import *
from .on_gateway_error import *
from .on_ready import *
from .on_resumed import *
from .on_shard_connect import *
from .on_shard_disconnect import *
from .on_shard_ready import *
from .on_shard_resumed import *
from .on_socket_event_type import *
from .on_guild_channel_delete import *
from .on_guild_channel_create import *
from .on_guild_channel_update import *
from .on_guild_channel_pins_update import *
from .on_private_channel_update import *
from .on_private_channel_pins_update import *
from .on_thread_create import *
from .on_thread_join import *
from .on_thread_member_join import *
from .on_thread_member_remove import *
from .on_thread_remove import *
from .on_thread_update import *
from .on_thread_delete import *
from .on_webhooks_update import *
from .on_guild_join import *
from .on_guild_remove import *
from .on_guild_update import *
from .on_guild_available import *
from .on_guild_unavailable import *
from .on_application_command_permissions_update import *
from .on_automod_action_execution import *
from .on_automod_rule_create import *
from .on_automod_rule_update import *
from .on_automod_rule_delete import *
from .on_guild_emojis_update import *
from .on_guild_integrations_update import *
from .on_integration_create import *
from .on_integration_update import *
from .on_invite_create import *
from .on_invite_delete import *
from .on_member_join import *
from .on_member_remove import *
from .on_member_update import *
from .on_member_ban import *
from .on_member_unban import *
from .on_presence_update import *
from .on_user_update import *
from .on_guild_scheduled_event_create import *
from .on_guild_scheduled_event_delete import *
from .on_guild_scheduled_event_update import *
from .on_guild_scheduled_event_subscribe import *
from .on_guild_scheduled_event_unsubscribe import *
from .on_stage_instance_create import *
from .on_stage_instance_delete import *
from .on_stage_instance_update import *
from .on_guild_stickers_update import *
from .on_guild_role_create import *
from .on_guild_role_delete import *
from .on_guild_role_update import *
from .on_voice_state_update import *
from .on_application_command import *
from .on_application_command_autocomplete import *
from .on_button_click import *
from .on_dropdown import *
from .on_interaction import *
from .on_message_interaction import *
from .on_modal_submit import *
from .on_message import *
from .on_message_delete import *
from .on_message_edit import *
from .on_bulk_message_delete import *
from .on_reaction_add import *
from .on_reaction_remove import *
from .on_reaction_clear import *
from .on_reaction_clear_emoji import *
from .on_typing import *
from .on_command_error import *
from .on_slash_command_error import *
from .on_user_command_error import *
from .on_message_command_error import *
from .on_command import *
from .on_slash_command import *
from .on_user_command import *
from .on_message_command import *
from .on_command_completion import *
from .on_slash_command_completion import *
from .on_user_command_completion import *
from .on_message_command_completion import *

def setup(bot):
   bot.add_cog(On_connect(bot))
   bot.add_cog(On_disconnect(bot))
   bot.add_cog(On_error(bot))
   bot.add_cog(On_gateway_error(bot))
   bot.add_cog(On_ready(bot))
   bot.add_cog(On_resumed(bot))
   bot.add_cog(On_shard_connect(bot))
   bot.add_cog(On_shard_disconnect(bot))
   bot.add_cog(On_shard_ready(bot))
   bot.add_cog(On_shard_resumed(bot))
   bot.add_cog(On_socket_event_type(bot))
   bot.add_cog(On_guild_channel_delete(bot))
   bot.add_cog(On_guild_channel_create(bot))
   bot.add_cog(On_guild_channel_update(bot))
   bot.add_cog(On_guild_channel_pins_update(bot))
   bot.add_cog(On_private_channel_update(bot))
   bot.add_cog(On_private_channel_pins_update(bot))
   bot.add_cog(On_thread_create(bot))
   bot.add_cog(On_thread_join(bot))
   bot.add_cog(On_thread_member_join(bot))
   bot.add_cog(On_thread_member_remove(bot))
   bot.add_cog(On_thread_remove(bot))
   bot.add_cog(On_thread_update(bot))
   bot.add_cog(On_thread_delete(bot))
   bot.add_cog(On_webhooks_update(bot))
   bot.add_cog(On_guild_join(bot))
   bot.add_cog(On_guild_remove(bot))
   bot.add_cog(On_guild_update(bot))
   bot.add_cog(On_guild_available(bot))
   bot.add_cog(On_guild_unavailable(bot))
   bot.add_cog(On_application_command_permissions_update(bot))
   bot.add_cog(On_automod_action_execution(bot))
   bot.add_cog(On_automod_rule_create(bot))
   bot.add_cog(On_automod_rule_update(bot))
   bot.add_cog(On_automod_rule_delete(bot))
   bot.add_cog(On_guild_emojis_update(bot))
   bot.add_cog(On_guild_integrations_update(bot))
   bot.add_cog(On_integration_create(bot))
   bot.add_cog(On_integration_update(bot))
   bot.add_cog(On_invite_create(bot))
   bot.add_cog(On_invite_delete(bot))
   bot.add_cog(On_member_join(bot))
   bot.add_cog(On_member_remove(bot))
   bot.add_cog(On_member_update(bot))
   bot.add_cog(On_member_ban(bot))
   bot.add_cog(On_member_unban(bot))
   bot.add_cog(On_presence_update(bot))
   bot.add_cog(On_user_update(bot))
   bot.add_cog(On_guild_scheduled_event_create(bot))
   bot.add_cog(On_guild_scheduled_event_delete(bot))
   bot.add_cog(On_guild_scheduled_event_update(bot))
   bot.add_cog(On_guild_scheduled_event_subscribe(bot))
   bot.add_cog(On_guild_scheduled_event_unsubscribe(bot))
   bot.add_cog(On_stage_instance_create(bot))
   bot.add_cog(On_stage_instance_delete(bot))
   bot.add_cog(On_stage_instance_update(bot))
   bot.add_cog(On_guild_stickers_update(bot))
   bot.add_cog(On_guild_role_create(bot))
   bot.add_cog(On_guild_role_delete(bot))
   bot.add_cog(On_guild_role_update(bot))
   bot.add_cog(On_voice_state_update(bot))
   bot.add_cog(On_application_command(bot))
   bot.add_cog(On_application_command_autocomplete(bot))
   bot.add_cog(On_button_click(bot))
   bot.add_cog(On_dropdown(bot))
   bot.add_cog(On_interaction(bot))
   bot.add_cog(On_message_interaction(bot))
   bot.add_cog(On_modal_submit(bot))
   bot.add_cog(On_message(bot))
   bot.add_cog(On_message_delete(bot))
   bot.add_cog(On_message_edit(bot))
   bot.add_cog(On_bulk_message_delete(bot))
   bot.add_cog(On_reaction_add(bot))
   bot.add_cog(On_reaction_remove(bot))
   bot.add_cog(On_reaction_clear(bot))
   bot.add_cog(On_reaction_clear_emoji(bot))
   bot.add_cog(On_typing(bot))
   bot.add_cog(On_command_error(bot))
   bot.add_cog(On_slash_command_error(bot))
   bot.add_cog(On_user_command_error(bot))
   bot.add_cog(On_message_command_error(bot))
   bot.add_cog(On_command(bot))
   bot.add_cog(On_slash_command(bot))
   bot.add_cog(On_user_command(bot))
   bot.add_cog(On_message_command(bot))
   bot.add_cog(On_command_completion(bot))
   bot.add_cog(On_slash_command_completion(bot))
   bot.add_cog(On_user_command_completion(bot))
   bot.add_cog(On_message_command_completion(bot))