# Bale AI Bot for Job Candidate Screening and Sentiment Analysis

This bot helps you with hiring using AI. It works with the Bale Messenger app.

## What it Does

This bot uses Artificial Intelligence (AI) to:

* **Check Job Titles:** If you type something, it can tell if it's a job title.
* **Help with Hiring:** If you tell it a job, it can help you choose the best people for the job by looking at their personality.
* **Suggest Interviews:** It can tell you what kind of interview to have with someone and when might be a good time, based on their personality.
* **Match People to Jobs:** For each job, it can tell you what kind of personality might be a good fit.
* **Understand Feelings:** If you type something that's not about jobs, the bot tries to understand how you are feeling and says something nice to cheer you up.
* **Speaks Persian:** The bot mostly talks in Persian.

## How to Use It

Here's how to get the bot working:

1.  **You Need These Things First:**
    * **Python:** You need to have Python installed on your computer. It's like the language the bot speaks.
    * **Bale Bot Token:** You need a special code (token) from Bale to tell Bale it's your bot.
    * **OpenAI Key:** This bot uses a smart AI from a company called OpenAI. You need a special key to use their AI. You get this key from a website (api.metisai.ir).

2.  **Get the Bot's Code:**
    * Go to this website: [https://github.com/mohoja313/Bale-JobSense](https://github.com/mohoja313/Bale-JobSense)
    * Click the green button that says "Code".
    * Click "Download ZIP".
    * Save the file on your computer and then open it (unzip it).

3.  **Install What the Bot Needs:**
    * Open a special program on your computer called "Terminal" (on Mac/Linux) or "Command Prompt" (on Windows).
    * Go to the folder where you saved the bot's code. You can use commands like `cd` to move between folders.
    * Type this command and press Enter: `pip install openai bale-bot`
        * This will install some extra tools the bot needs to work.

4.  **Tell the Bot Your Special Codes:**
    * Open the file with the bot's code (it probably ends with `.py`, like `main.py` or `bot.py`). You can use a simple text editor to open it.
    * Look for these lines in the code:
        ```python
        client = Bot(token="your bot token")
        clientb = OpenAI(base_url="[https://api.metisai.ir/openai/v1](https://api.metisai.ir/openai/v1)", api_key="Your model key")
        ```
    * Replace `"your bot token"` with the special code you got from Bale. Make sure to keep the quotation marks.
    * Replace `"Your model key"` with the special code you got from the OpenAI website (api.metisai.ir). Again, keep the quotation marks.
    * Save the file.

5.  **Run the Bot:**
    * Go back to the "Terminal" or "Command Prompt".
    * Make sure you are still in the folder with the bot's code.
    * Type this command and press Enter: `python your_bot_script.py` (replace `your_bot_script.py` with the actual name of the file).
    * The bot should start running. You will see a message in the "Terminal" or "Command Prompt" saying it's ready.

## How to Talk to the Bot

Open the Bale Messenger app and find your bot. You can talk to it using these commands:

* **/start:** Type `/start` and send it. The bot will say hello in Persian and ask what job you are thinking about.
* **/message:** Type `/message` and send it. The bot will ask you to type your message.
    * **If you type a job name (in Persian):** The bot will try to help you with hiring for that job.
    * **If you type something else (in Persian):** The bot will try to understand your feelings and say something nice.

## What the Code Does (For People Who Know a Little Python)

The code has different parts that do different things:

* **`on_ready()`:** This part runs when the bot starts and tells you it's ready.
* **`on_update()`:** This part keeps track of what's happening in the bot.
* **`on_message()`:** This is the main part that looks at the messages you send to the bot.
    * If you send `/start`, it sends a welcome message.
    * If you send `/message`, it waits for your next message.
        * It checks if your message is a job title by asking OpenAI (the smart AI).
        * If it's a job title, it looks at a list of fake people (candidates) and tries to match them to the job based on their personality. It also suggests when and how to interview them.
        * If it's not a job title, it asks OpenAI to understand your feelings and sends you a comforting message.

* There is a list called `candidates` which has some example people with their names, emails, and personality types.

## If You Want to Help Make the Bot Better

If you know how to code in Python and want to help make this bot better, you are welcome to! You can look at the code and see if you can add new features or fix any problems.

## License

This project uses the MIT License. This means you can use and share the code, but you need to give credit to the original creator.

## Thank You

Thank you for checking out this bot!
