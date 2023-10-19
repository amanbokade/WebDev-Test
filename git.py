import os

def makeCommitOnDay(day: int, total_days: int):
    if day < 1 or day > total_days:
        print("Invalid day. Please choose a day within the range.")
        return

    date_to_commit = f"{day} days ago"
    with open('data.txt', 'a') as file:
        file.write(f'{date_to_commit} <- this was the commit for the day!!\n')

    os.system('git add data.txt')
    os.system(f'git commit --date="{date_to_commit}" -m "Commit for day {day}"')
    os.system('git push')

total_days = 80  # Total number of days in the range
chosen_day = 42  # Specify the day on which you want to make a commit

makeCommitOnDay(chosen_day, total_days)


