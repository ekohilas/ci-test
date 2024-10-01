import dataclasses


class Rule: ...


@dataclasses.dataclass(frozen=True)
class IfRule(Rule):
    condition: str

    def __str__(self):
        return self.condition


@dataclasses.dataclass(frozen=True)
class GlobPath:
    glob_path: str


@dataclasses.dataclass(frozen=True)
class ChangesRule(Rule):
    changes: tuple[GlobPath]

    def __str__(self):
        return "\n".join(change.glob_path for change in self.changes)


@dataclasses.dataclass(frozen=True)
class CombinationRule(Rule):
    if_rule: IfRule
    changes_rule: ChangesRule

    def __str__(self):
        return f"{self.if_rule}\n{self.changes_rule}"


@dataclasses.dataclass(frozen=True)
class CiJob:
    name: str
    rules: tuple[Rule]


class JobRulesParser:
    def get_jobs(self) -> list[CiJob]:
        raise NotImplementedError
