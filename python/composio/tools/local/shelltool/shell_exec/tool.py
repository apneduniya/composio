"""Tool for executing shell commands."""

import typing as t

from composio.tools.base.local import LocalAction, LocalTool
from composio.tools.local.shelltool.shell_exec.actions.exec import ExecCommand
from composio.tools.local.shelltool.shell_exec.actions.new import CreateShell
from composio.tools.local.shelltool.shell_exec.actions.spawn import SpawnProcess


class Shelltool(LocalTool, autoload=True):
    """Tool for executing shell commands."""

    @classmethod
    def actions(cls) -> t.List[t.Type[LocalAction]]:
        """Returns list of actions."""
        return [
            ExecCommand,
            CreateShell,
            SpawnProcess,
        ]
