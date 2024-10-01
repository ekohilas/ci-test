import dataclasses


@dataclasses.dataclass(frozen=True)
class IfRule:
    condition: str

    def __str__(self):
        return self.condition


@dataclasses.dataclass(frozen=True)
class GlobPath:
    glob_path: str


@dataclasses.dataclass(frozen=True)
class ChangesRule:
    changes: tuple[GlobPath]

    def __str__(self):
        return "\n".join(change.glob_path for change in self.changes)


@dataclasses.dataclass(frozen=True)
class Rule:
    if_rule: IfRule | None
    changes_rule: ChangesRule | None

    def __str__(self):
        if_rule = str(self.if_rule) if self.if_rule else ""
        changes_rule = str(self.changes_rule) if self.changes_rule else ""
        return "\n".join((if_rule, changes_rule))


@dataclasses.dataclass(frozen=True)
class CiJob:
    name: str
    rules: tuple[Rule]


class JobRulesParser:
    def get_jobs(self) -> list[CiJob]:
        raise NotImplementedError
