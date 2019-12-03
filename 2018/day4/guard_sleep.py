import re
import datetime
from enum import Enum
from collections import defaultdict


class GuardStateChange(Enum):
    start_shift = 1,
    sleep = 2,
    awaken = 3


class TimelineAction:
    def __init__(self, timestamped_action_string):
        self.guard_id = None
        match = re.search("\[(.*)\] (.*)", timestamped_action_string)
        self.timestamp = datetime.datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
        action_string = match.group(2)
        action_match = re.search("Guard #(\d+) begins shift", action_string)
        if action_match:
            self.guard_id = int(action_match.group(1))
            self.guard_state_change = GuardStateChange.start_shift
        elif action_string == "wakes up":
            self.guard_state_change = GuardStateChange.awaken
        else:
            self.guard_state_change = GuardStateChange.sleep

    def __lt__(self, other):
        return self.timestamp < other.timestamp


guard_actions = []
with open("guard_schedule.txt", "r") as guard_actions_file:
    for guard_action_string in guard_actions_file:
        guard_actions.append(TimelineAction(guard_action_string))

guard_actions.sort()

guard_sleep_by_day_by_id = defaultdict(lambda: defaultdict(list))

guard_id = None
guard_sleep_start = None
guard_awaken = None

for guard_action in guard_actions:
    if guard_action.guard_id:
        guard_id = guard_action.guard_id
    elif guard_action.guard_state_change == GuardStateChange.sleep:
        guard_sleep_start = guard_action.timestamp.minute
    else:
        guard_awaken = guard_action.timestamp.minute
        guard_sleep_by_day_by_id[guard_id][guard_action.timestamp.day].append((guard_sleep_start, guard_awaken))


def count_sleeping_minutes(guard_id):
    sleep_by_day = guard_sleep_by_day_by_id[guard_id]
    sleep_minutes = 0
    for day, sleep_list in sleep_by_day.items():
        for nap in sleep_list:
            sleep_minutes += nap[1] - nap[0]
    return sleep_minutes


def minute_most_slept(guard_id):
    sleep_by_day = guard_sleep_by_day_by_id[guard_id]
    minute_sleep_frequency = defaultdict(int)
    for day, sleep_list in sleep_by_day.items():
        for nap in sleep_list:
            for minute in range(nap[0], nap[1]):
                minute_sleep_frequency[minute] += 1
    most_slept_minute = max(minute_sleep_frequency, key=minute_sleep_frequency.get)
    minute_frequency = minute_sleep_frequency[most_slept_minute]
    return most_slept_minute, minute_frequency


sorted_guards = sorted(guard_sleep_by_day_by_id.keys(), key=count_sleeping_minutes)
target_guard = sorted_guards[-1]
target_minute, _ = minute_most_slept(target_guard)
print("guard {} slept the most minutes".format(target_guard))
print("most frequent sleeping minute", target_minute)
print("answer #1:", target_guard * target_minute)

sorted_guards = sorted(guard_sleep_by_day_by_id.keys(), key=lambda guard_id: minute_most_slept(guard_id)[1])
target_guard = sorted_guards[-1]
target_minute, frequency = minute_most_slept(target_guard)
print("guard {} had the target minute".format(target_guard))
print("most slept minute for target guard was {} with frequency {}".format(target_minute, frequency))
print("answer #2:", target_guard * target_minute)
