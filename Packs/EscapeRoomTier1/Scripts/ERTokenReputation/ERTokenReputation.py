import traceback
from typing import Any, Dict

import demistomock as demisto
from CommonServerPython import *  # noqa: E402 lgtm [py/polluting-import]

# COMMAND FUNCTION #


def validate_token(token):
    if token.lower() != 'the auto extract feature':
        raise ValueError('Unsupported indicator. Try another one...')


def reputation_command(args: Dict[str, Any]) -> CommandResults:
    token = args.get('token', '')

    markdown = f'## {token}\n\nArgs:{args}'
    demisto.info(markdown)

    validate_token(token)

    return CommandResults(
        readable_output=markdown,
    )


# MAIN FUNCTION #


def main():
    try:
        return_results(reputation_command(demisto.args()))
    except Exception as exc:  # pylint: disable=W0703
        demisto.error(traceback.format_exc())  # print the traceback
        return_error(f'Failed to execute ERTokenReputation. Error: {str(exc)}')


# ENTRY POINT #


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()