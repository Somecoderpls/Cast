from dataclasses import dataclass

@dataclass
class RuleBreak:
    """ A collection of Rules to look for when scanning files.

        Attributes:
            id (str): The ID used to identify the rule.
            message (str): The message to post for the rule.
            func (list): List of functions to look for.
            args (list): List of arguments to look for.
            arg_pos (int): The position to look for arguments at.
    """
    id: str
    message: str
    func: list
    args: list
    arg_pos: int

@dataclass
class Finding:
    """ A collection of Findings to look for when scanning files.

        Attributes:
            id (str): The ID used to identify the rule.
            message (str): The message to post for the rule.
            line (int): The line the error is found at.
            column (int): The column the error is found at.
    """
    id: str
    message: str
    line: int
    column: int

class Findings():
    """ Findings of potential issues.

        Args:
            rule_id (str): The ID of the RuleBreak dataclass.
            message (str): The message used for the RuleBreak dataclass.
            line (int): The line number the issue can be found at.
            column (int): The column offset the issue can be found at.
    """
    def __init__(self, rule_id, message, line, column):
        self._findings = Finding(
            rule_id,
            message,
            line,
            column
        )

    def __str__(self):
        """ String representation of the findings dictionary.
            
            Returns:
                str: A formatted string representation of the findings dictionary.
        """
        return f"Issue found!\n ID: {self._findings.id}\n Message: {self._findings.message}\n At line: {self._findings.line}\n At column: {self._findings.column}\n"

    def set_findings(self, rule_id, message, line, column):
        """ Update the findings dictionary with new values.

            Args:
                rule_id (str): The ID of the RuleBreak dataclass.
                message (str): The message used for the RuleBreak dataclass.
                line (int): The line number the issue can be found at.
                column (int): The column offset the issue can be found at.
        """
        self._findings = Finding(rule_id, message, line, column)

    def get_finding(self, entry):
        """ Get an entry of the findings dictionary.
        
            Returns:
                int or str: The value of the findings dictionary entry.
        """
        if not hasattr(self._findings, entry):
            raise AttributeError(f"Unknown attribute {entry} in dataclass")

        return getattr(self._findings, entry)


