import dataclasses


@dataclasses.dataclass(frozen=True)
class IfRule:
    condition: str


@dataclasses.dataclass(frozen=True)
class GlobPath:
    glob_path: str


@dataclasses.dataclass(frozen=True)
class ChangesRule:
    changes: tuple[GlobPath]


@dataclasses.dataclass(frozen=True)
class Rule:
    if_rule: IfRule | None
    changes_rule: ChangesRule | None

    @classmethod
    def make_empty(cls) -> "Rule":
        return cls(
            if_rule=None,
            changes_rule=None,
        )


@dataclasses.dataclass(frozen=True)
class CiJob:
    name: str
    rules: tuple[Rule]


class JobRulesParser:
    def get_jobs(self) -> list[CiJob]:
        raise NotImplementedError
