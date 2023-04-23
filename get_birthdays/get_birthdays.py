import os

from pathlib import Path
from datetime import datetime, timedelta


# ----------Users list prepairing----------
def get_users_list(settings_path: Path) -> list:
    users = []
    with open(Path(settings_path), 'r') as settings_file:
        for line in settings_file:
            users.append({'name': line.split(':')[0], 'birthday': (datetime.strptime((line.split(':')[1]).strip(), '%Y.%m.%d')).date()})
    return users


# ----------Next week calculating----------
current_datetime = datetime.now().date()
# current_week_start = datetime.now().date() - timedelta(days=current_datetime.weekday())
# next_week_start = current_week_start + timedelta(weeks=1)
# next_week_end = next_week_start + timedelta(days=6)
next_week = current_datetime + timedelta(days=6)


# ----------Birthdays checking----------
def get_birthdays_per_week(users: list) -> None:
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saturday = []
    sunday = []
    for item in users:
        _date = datetime(year=datetime.now().year, month=item['birthday'].month, day=item['birthday'].day)
        if current_datetime <= _date.date() <= next_week:
            match _date.weekday():
                case 0:
                    monday.append(item['name'])
                case 1:
                    tuesday.append(item['name'])
                case 2:
                    wednesday.append(item['name'])
                case 3:
                    thursday.append(item['name'])
                case 4:
                    friday.append(item['name'])
                case 5:
                    saturday.append(item['name'])
                case 6:
                    monday.append(f"{item['name']} (birthday is on Sunday)")
    if monday:
        print(f"Monday: {', '.join(monday)}")
    if tuesday:
        print(f"Tuesday: {', '.join(tuesday)}")
    if wednesday:
        print(f"Wednesday: {', '.join(wednesday)}")
    if thursday:
        print(f"Thursday: {', '.join(thursday)}")
    if friday:
        print(f"Friday: {', '.join(friday)}")
    if saturday:
        print(f"Saturday: {', '.join(saturday)}")


# ----------Entry point----------
if __name__ == '__main__':
    print(f'From {current_datetime} to {next_week}')
    get_birthdays_per_week(get_users_list('settings.txt'))

def main() -> None:
    while True:
        user_input = input('Specify the path to the settings.txt file or press enter to cancelling: ')
        if os.path.isfile(user_input):
            print('Processing...')
            print(f'From {current_datetime} to {next_week}')
            get_birthdays_per_week(get_users_list(user_input))
            print('Successful')
            break
        elif user_input == '':
            break
        else:
            print('File not found. Please, try again.')
   
    
