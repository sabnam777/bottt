from bot import dp, executor

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
