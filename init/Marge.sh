export SEMAPHORE_PROJECT_DIR=`pwd`
. "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"/telegram
TELEGRAM_TOKEN=${BOT_API_KEY}
export BOT_API_KEY TELEGRAM_TOKEN
tg_sendinfo "<code>I am gonna merge staging into master</code>"
cd
git clone https://github.com/RaphielGang/Telegram-UserBot.git
cd Telegram-UserBot
git remote rm origin
git remote add origin https://baalajimaestro:${GH_PERSONAL_TOKEN}@github.com/raphielgang/telegram-userbot.git
git fetch
git checkout staging
git pull origin staging
git push --force origin staging:master
tg_sendinfo "<code>I have merged all commits from staging into master</code>"
