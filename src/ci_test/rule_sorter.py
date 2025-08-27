class RuleSorter:
    def sort_function(
        self,
        # TODO: Update type
        json_object: dict[str, list[str] | str],
    ) -> tuple:
        return (
            # order by existance of: none, if, changes
            tuple(reversed((
                "if" in json_object,
                "changes" in json_object,
            ))),
            # then order values alphabetically
            json_object.get("if", ""),
            json_object.get("changes", []),
            json_object["jobs"],
        )
