class ParseShowCommandFunction:
    @staticmethod
    def parse_show_command(steps, device, command_name: str):
        with steps.start(f"Parsing {command_name}", continue_=True) as step:
            try:
                return device.parse(command_name)
            except Exception as e:
                step.failed('Could not parse it correctly\n{e}'.format(e=e))
                return None