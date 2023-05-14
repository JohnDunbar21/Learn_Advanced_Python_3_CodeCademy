# Logging with Python 3

By importing Python's `logging` module, we can:
- Identify the data and time of a custom/error message;
- Format logs to make debugging easier;
- Set severity levels for the logs;
- Output the logs to various streams.

## Dated Timestamps

The Python `logging` module provides a formatting option to include dated timestamps for logged messages.

## Additional Formatting Options

The `logging` module provides several options for formatting what information is included in the log message and how that information appears, such as the module name where the logged message originated from or even the specific line of code that it refers to.

**Doing this enables programmers to debug much more effectively**.

## Severity Level

There are different levels of severity for logs, including:
- notset;
- debug;
- info;
- warning;
- error;
- critical.

This is a great alternative to `print` statements as, once fully functional, we can filter out any log statements that have a debug severity level by setting a log level for the logger.

## Log Files

Logs can be saved to files, allowing the log messages to be accessed beyond code execution time: additionally, the saved log file can then be indexed and made searchable.