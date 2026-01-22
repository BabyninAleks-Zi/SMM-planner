import telegram
from environs import Env



def publish_post_to_tg(chat_id, bot, text: str, photo = None):
		if photo:
			result = bot.send_photo(chat_id=chat_id, photo=photo, caption=text)
			return result['message_id']
		if not photo:
			result = bot.send_message(chat_id=chat_id, text=text)
			return result['message_id']


def delete_post_from_tg(bot, chat_id, post_id):
	try:
		result = bot.delete_message(chat_id=chat_id, message_id=post_id)
		return result
	except:
		print('ошибка')

	# доделать отработку, если пользователь передает только текст или только фото