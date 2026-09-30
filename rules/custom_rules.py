from .base import BaseRule
from .models import RuleBreak

class PopenRule(BaseRule):
    def __init__(self):
        super().__init__()
        self.rulebreak = RuleBreak(
            id="PYT001",
            message="!!WARNING!! POpen with shell used.",
            func=["subprocess", "Popen"],
            args=["shell"],
            arg_pos = -1
        )

class PickleRule(BaseRule):
    def __init__(self):
        super().__init__()
        self.rulebreak = RuleBreak(
            id="PYT002",
            message="!!WARNING!! pickle.loads being used.",
            func=["pickle", "loads"],
            args=[],
            arg_pos = -1
        )

class OsJoinRule(BaseRule):
    def __init__(self):
        super().__init__()
        self.rulebreak = RuleBreak(
            id="PYT003",
            message="!!WARNING!! path.join being used with a root argument.",
            func=["os", "path", "join"],
            args=["/"],
            arg_pos = 1
        )

class PathJoinRule(BaseRule):
    def __init__(self):
        super().__init__()
        self.rulebreak = RuleBreak(
            id="PYT004",
            message="!!WARNING!! joinpath being used with a root argument.",
            func=["pathlib", "Path", "joinpath"],
            args=["/"],
            arg_pos = 1
        )

class YamlLoadRule(BaseRule):
    def __init__(self):
        super().__init__()
        self.rulebreak = RuleBreak(
            id="PYT005",
            message="!!WARNING!! yaml.load being used. Make sure to use yaml.safe_load where possible.",
            func=["yaml", "load"],
            args=[],
            arg_pos = -1
        )

class UrlJoinRule(BaseRule):
    def __init__(self):
        super().__init__()
        self.rulebreak = RuleBreak(
            id="PYT006",
            message="!!WARNING!! urllib.parse.urljoin being used with an absolute URL argument.",
            func=["urllib", "parse", "urljoin"],
            args=["https://", "http://"],
            arg_pos = 1
        )
