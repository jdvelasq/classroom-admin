from colorama import Fore, Style, init

init(autoreset=True)


def make_colorized_prompt(prompt):

    separator = Fore.LIGHTBLACK_EX + ":" + Style.RESET_ALL

    parts = prompt.split(":")
    parts = [part.strip() for part in parts]

    colorized_prompt = [Fore.LIGHTBLACK_EX + parts[0] + ":" + Style.RESET_ALL]

    for index, part in enumerate(parts[1:]):
        if str(part) == "none":
            colorized_prompt.append(Fore.LIGHTBLACK_EX + "none" + Style.RESET_ALL)
        else:
            colorized_prompt.append(part)

        if index < len(parts) - 2:
            colorized_prompt.append(Fore.LIGHTBLACK_EX + ":" + Style.RESET_ALL)
        else:
            colorized_prompt.append(Fore.LIGHTBLACK_EX + " > " + Style.RESET_ALL)

    return "".join(colorized_prompt)
