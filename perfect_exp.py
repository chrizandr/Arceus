# Credit to Shiva for writing this script
# https://gist.github.com/Coldsp33d/18f65a990069ae98744b8cd829e70ebb

import requests
import pandas as pd
import numpy as np
import datetime
import pytz
import warnings
warnings.filterwarnings("ignore")

import discord

def is_east_coast_daytime():
    # Get the current time in the Eastern timezone
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.datetime.now(eastern)

    # Check if the current time is between 6AM and 6PM EST
    return current_time.hour >= 6 and current_time.hour < 18


def find_optimal_trainers(current_exp, desired_exp, table, use_exp_night=False):
    """
    Finds the optimal trainers to fight and the amount of times to fight them to get as close to desired_exp as possible
    without exceeding it, given starting exp current_exp and desired exp desired_exp, and a table of trainers and their exp gains.
    The table has the following columns: "name", "expDay" (i.e., exp earned per battle during the day), and "expNight"
    (i.e., exp earned per battled during the night). If use_exp_night is True, uses only expNight to calculate the final result;
    otherwise, use only expDay.

    Returns a dictionary of trainer names and non-zero battle counts.
    """
    # Compute the exp difference and filter out trainers with negative exp gains
    exp_gain = np.where(use_exp_night, table['expNight'], table['expDay'])  # Use expNight if use_exp_night is True; expDay otherwise
    table_filtered = table.loc[exp_gain <= (desired_exp - current_exp)].copy()  # Filter out trainers with negative exp gains

    # Sort the table by exp gains in descending order
    exp_gain_sorted = np.where(use_exp_night, table_filtered['expNight'], table_filtered['expDay'])
    table_sorted = table_filtered.iloc[np.argsort(exp_gain_sorted)[::-1]]

    # Initialize the result dictionary and compute the remaining exp to gain
    trainers = {}
    remaining_exp = desired_exp - current_exp
    current_exp2 = current_exp

    # Iterate over the trainers in the sorted table and compute the number of battles for each
    for index, row in table_sorted.iterrows():
        exp_gain = row['expNight'] if use_exp_night else row['expDay']
        exp_diff = exp_gain - remaining_exp
        if exp_diff > 0:
            continue
        num_battles = int(remaining_exp / exp_gain)
        if num_battles > 0:
            trainers[(row['name'], row["number"])] = [num_battles, exp_gain]
            remaining_exp -= num_battles * exp_gain
            current_exp2 += num_battles * exp_gain
        if remaining_exp <= 0:
            break

    return trainers


def get_perfect_exp(level, ceil=False):
    if ceil:
        return ((level + 1) ** 3) - 1
    return (level ** 3) + 1


def verify_exp(table, current_exp, required_exp):
    exp_gained = 0
    required_gain = required_exp - current_exp

    for trainer in table:
        num_battles, exp = table[trainer]
        exp_gained += num_battles * exp

    return required_gain == exp_gained


def perfect_exp(X, Y):
    url = 'https://wiki.tppc.info/Training_Accounts'
    response = requests.get(url)
    table_list = pd.read_html(response.text)

    # Extract the first table from the list (which should be the training accounts table)
    table = table_list[1]
    table = table[['Trainer Name', 'Number', 'Exp. (Day)', 'Exp. (Night)']]

    # Rename the remaining columns
    table.columns = ['name', 'number', 'expDay', 'expNight']
    table = table.append({'name': 'Single Milotic lvl 5', 'number': 24659, 'expDay': 300, 'expNight' : 300}, ignore_index=True)
    table = table.append({'name': 'Single Shedinja', 'number': 2380615, 'expDay': 3, 'expNight' : 3}, ignore_index=True)
    table = table.append({'name': 'Shedinja w/ 2 Exp shares', 'number': 2380615, 'expDay': 1, 'expNight' : 1}, ignore_index=True)


    trainers = find_optimal_trainers(X, Y, table, use_exp_night=not is_east_coast_daytime())
    return trainers


def format_output(table, current_exp, desired_exp):
    sep = "______" * 10
    embed = discord.Embed(title="Battle summary", description="These calculations are based on the info on Wiki. Please use at your own risk",
                          color=discord.Color.green())

    embed.add_field(name="Current Exp", value=str(current_exp), inline=True)
    embed.add_field(name="Desired Exp", value=str(desired_exp)+f'\n{sep}', inline=False)

    for entry in table:
        name, number = entry
        num_battles, exp = table[entry]
        embed.add_field(name="Info", value=str(name), inline=True)
        embed.add_field(name="ID", value=str(number), inline=True)
        embed.add_field(name="Num Battles", value=str(num_battles), inline=True)
        current_exp += num_battles * exp
        embed.add_field(name="Exp after", value=str(current_exp)+f'\n{sep}', inline=False)


    # embed.add_field(name="Ungendered", value=str(index_entry['ungendered']), inline=True)
    # embed.add_field(name="Genderless", value=str(index_entry['genderless']), inline=True)
    return embed


def perfect_exp_handler(message):
    values = message.content.split()
    response = "Use this format ffs ```!perfect <current exp> <desired exp>\n!perfect level <current exp> <desired level>```"
    if len(values) == 3 or (len(values) == 4 and values[1] == "level"):
        if len(values) == 3:
            if not values[1].isdecimal() or not values[2].isdecimal():
                return response
            current_exp = int(values[1].replace(",", ""))
            desired_exp = int(values[2].replace(",", ""))
        elif len(values) == 4:
            if not values[2].isdecimal() or not values[3].isdecimal():
                return response
            current_exp = int(values[2].replace(",", ""))
            desired_exp = get_perfect_exp(int(values[3].replace(",", "")))

        if desired_exp <= current_exp:
            response = "Desired Exp is less than Current Exp mf. Ask Shrimpy to do that."
        else:
            response = format_output(perfect_exp(current_exp, desired_exp), current_exp, desired_exp)

    return response
