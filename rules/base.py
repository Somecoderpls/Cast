import ast
from .models import RuleBreak, Findings

class BaseRule(ast.NodeVisitor):
    """ Base Rule class for functions.
    """
    def __init__(self):
        self.rulebreak = RuleBreak(
            id="PYB001",
            message="Default error message for base class",
            func=[],
            args=[],
            arg_pos = -1
        )
        self.findings = Findings(
            self.rulebreak.id,
            self.rulebreak.message,
            0,
            0
        )

    def _get_string_args(self, node_arg) -> str:
        """ Get args as strings.

            Returns:
                str: Returns the arg as a string from the node, otherwise an empty string.
        """
        if isinstance(node_arg, ast.Constant) and isinstance(node_arg.value, str):
            return node_arg.value
        # This needs to be here for older python versions.
        elif isinstance(node_arg, ast.Str):
            return node_arg.s
        return str()

    def _find_func(self, node):
        """ Find the function, in the node, defined by the rule.

            Returns:
                bool: True if found, false if not.
        """
        if isinstance(node.func, ast.Attribute):
            return True
        if isinstance(node.func, ast.Name):
            return True
        return False

    def _find_arg(self, node):
        """ Find the args, in the node, defined by the rule.

            Returns:
                bool: True if found, false if not.
        """
        if not self.rulebreak.args:
            return True

        pos = self.rulebreak.arg_pos
        if 0 <= pos < len(node.args):
            arg_get = self._get_string_args(node.args[pos])
            if not arg_get:
                return False
            if len(self.rulebreak.args) == 1:
                if arg_get.startswith(self.rulebreak.args[0]):
                    return True
            else:
                for arg_ in self.rulebreak.args:
                    if arg_get.startswith(arg_):
                        return True
        else:
            for kw in node.keywords:
                if kw.arg in self.rulebreak.args:
                    return True
        return False
 
    def visit_Call(self, node):
        """ Visits a Call node within the AST and checks if the rule's function name(s) and arg(s) are present.
            If they are update our findings and post it to the console.
        """
        if self._find_arg(node) and self._find_func(node):
            self.findings.set_findings(self.rulebreak.id, self.rulebreak.message, node.lineno, node.col_offset)
            print(self.findings)
        self.generic_visit(node)
