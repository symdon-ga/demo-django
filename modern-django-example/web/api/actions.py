import enum

@enum.unique
class CounterAction(enum.Enum):
    increment = 'increment'
    decrement = 'decrement'
