from fuzzywuzzy import process
from command_executor import CommandExecutor
import database


class Recognizer():

    def recognize(self, recognized_text, tag) -> bool:
        commands_with_tags = dict()
        commands_names = []
        for select_result in database.select_option(tag):
            commands_names.append(select_result[1])
            commands_with_tags[select_result[1]] = select_result[3]

        process_tag_selection = process.extractOne(recognized_text, commands_names)

        if (tag == "alias"):
            if (process_tag_selection[1] > 40): return True
            else: return False

        CommandExecutor()\
            .execute(
                {
                    "input_text" : recognized_text,
                    commands_with_tags[process_tag_selection[0]] : process_tag_selection
                }
            )


        return False
