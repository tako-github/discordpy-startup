from discord.ext import commands
import os
import traceback
import gspread

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
# スプシにアクセス
def connect_gspread(jsonf,key):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    return worksheet
# ここでjsonfile名ススプシのKeyを入力
jsonf = "./charsheet-313204-05c558660514.json"
spread_sheet_key = "1ZWJpxzc8h-XlamHuI6B4BqOx2s0iA5EuUTvR7_jzYnM"
ws = connect_gspread(jsonf,spread_sheet_key)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('返信')
    await ctx.send('返信')
    
bot.run(token)
