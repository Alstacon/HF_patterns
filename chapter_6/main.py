from chapter_6.remote_control import RemoteControlWithUndo
from chapter_6 import commands
from chapter_6 import devices


def program_slots():
    control = RemoteControlWithUndo(2)

    commands_map = {
        0:
            {
                'on': commands.TurnOnCommand(devices.bedroom_light),
                'off': commands.TurnOffCommand(devices.bedroom_light)
            },
        1:
            {
                'on': commands.TurnOnCommand(devices.garage_light),
                'off': commands.TurnOffCommand(devices.garage_light)
            },
        2:
            {
                'on': commands.MacroCommands([commands.TurnOnCommand(devices.bedroom_light),
                                              commands.TurnOnCommand(devices.garage_light)]),
                'off': commands.MacroCommands([
                    commands.TurnOffCommand(devices.bedroom_light),
                    commands.TurnOffCommand(devices.garage_light)
                ])
            }
    }

    for slot, command_set in commands_map.items():
        control.set_command(slot, command_set['on'], command_set['off'])

    return control


def use_rm_control():
    control = program_slots()

    print(control)

    control.on_button_pushed(0)
    print('-' * 10)

    control.undo_button_pushed()
    print('-' * 10)

    control.on_button_pushed(1)
    print('-' * 10)

    control.off_button_pushed(0)
    print('-' * 10)

    control.undo_button_pushed()
    print('-' * 10)

    control.on_button_pushed(1)
    print('-' * 10)

    control.off_button_pushed(0)
    print('-' * 10)

    control.off_button_pushed(1)
    print('-' * 10)



    control.on_button_pushed(2)
    print('-' * 10)




if __name__ == '__main__':
    use_rm_control()
