from collections import deque

from chapter_6.commands import Command, NoCommand


class RemoteControlWithUndo:
    """
    Remote controller with undo function and changeable amount of slots
    """

    def __init__(self, slots: int) -> None:
        self.slots = slots
        self._on_commands: dict[int, Command] = {
            i: NoCommand for i in range(self.slots)
        }
        self._off_commands: dict[int, Command] = {
            i: NoCommand for i in range(self.slots)
        }
        self._used_commands: deque[Command] = deque()

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_pushed(self, slot: int) -> None:
        self._on_commands[slot].execute()
        self._used_commands.append(self._on_commands[slot])

    def off_button_pushed(self, slot: int) -> None:
        self._off_commands[slot].execute()
        self._used_commands.append(self._off_commands[slot])

    @property
    def last_command(self):
        return self._used_commands.pop()

    def undo_button_pushed(self) -> None:
        self._used_commands.pop().undo()

    def __repr__(self) -> str:
        return (
            f'Remote controller on {self.slots} slots.\n'
            'ON commands: '
            f'{[command for command in self._on_commands.values()]}.\n'
            'OFF commands: '
            f'{[command for command in self._off_commands.values()]}.\n'
        )
