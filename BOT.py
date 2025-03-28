from openai import OpenAI
from bale import Bot, Update, Message
client = Bot(token="your bot token")

clientb = OpenAI(base_url="https://api.metisai.ir/openai/v1", api_key="Your model key")

@client.event
async def on_ready():
	print(client.user.username, "is Ready!")

@client.event
async def on_update(update: Update):
	print(update.update_id)

@client.event
async def on_message(message: Message):
	if message.content == '/start': # to get caption or text of message
		await message.reply('سلامِ، به ربات هوش مصنوعی خوش آمدید؛شغل مورد نظر خود را وارد کنید')

@client.event
async def on_message(message: Message):
    if message.content == '/message':
        await message.reply('پیام خود را وارد کنید')
        def answer_checker(m: Message):
            return message.author == m.author and bool(message.text)
        answer_obj: Message = await client.wait_for('message', check=answer_checker)
        user_input = answer_obj.content
        candidates = [
            {"name": "علی", "email": "ali@example.com", "mbti": "INTJ"},
            {"name": "بهرام", "email": "bahram@example.com", "mbti": "ENFP"},
            {"name": "فرهاد", "email": "farhad@example.com", "mbti": "ISTJ"},
            {"name": "سارا", "email": "sara@example.com", "mbti": "ESFJ"}
        ]
        prompt_check_job = f"Is '{user_input}' a job title? Please answer in Persian."
        response_check_job = clientb.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt_check_job}
            ]
        )

        is_job_title = response_check_job.choices[0].message.content

        if "بله" in is_job_title:
            # If it's a job title, provide personality analysis and interview details
            prompt = f"Based on the job '{user_input}', match the following users with their personality types and MBTI types, and determine the interview timeand say reson and paeameters for why chose this time:\n"
            for candidate in candidates:
                prompt += f"name: {candidate['name']}, email: {candidate['email']}, MBTI: {candidate['mbti']}\n"

            response_personality = clientb.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt + "\nPlease respond in Persian."}
                ]
            )
            return await answer_obj.reply(f"\nGPT Response:\n{response_personality.choices[0].message.content}\n")

        else:
            # If it's not a job title, analyze user's feelings
            prompt_feelings = f"Please analyze the following feelings and provide comfort to the user:\n{user_input}\n"
            response_feelings = clientb.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt_feelings + "\nPlease respond in Persian."}
                ]
            )

            return await answer_obj.reply(f"\nGPT Response:\n{response_feelings.choices[0].message.content}\n")

client.run()








    # Check if the input is a job title
