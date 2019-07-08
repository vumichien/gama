from contextlib import contextmanager
from typing import Iterator, Optional, NamedTuple
import logging

from .stopwatch import Stopwatch

log = logging.getLogger(__name__)


class Activity(NamedTuple):
    name: str
    stopwatch: Stopwatch
    time_limit: Optional[int] = None
    
    @property
    def time_left(self) -> float:
        """ Time left in seconds. Raises a TypeError if `time_limit` was not specified. """
        return self.time_limit - self.stopwatch.elapsed_time

    @property
    def exceeded_limit(self) -> float:
        """ True iff a limit was specified and its exceeded. False iff there is time left or no limit was specified. """
        return (self.time_limit is not None) and (self.time_limit - self.stopwatch.elapsed_time < 0)


class TimeKeeper:
    """ Simple object that helps keep track of time over multiple activities. """

    def __init__(self, total_time: int=0):
        self.total_time = total_time
        self.current_activity = None
        self.activities = []

    @property
    def total_time_remaining(self) -> float:
        """ Return time remaining in seconds. """
        if self.total_time > 0:
            return self.total_time - sum(map(lambda a: a.stopwatch.elapsed_time, self.activities))
        raise RuntimeError("Time Remaining only available if `total_time` was set on init.")

    @property
    def current_activity_time_elapsed(self) -> float:
        """ Return elapsed time in seconds of current activity. Raise RuntimeError if no current activity. """
        if self.current_activity is not None:
            return self.current_activity.stopwatch.elapsed_time
        else:
            raise RuntimeError("No activity in progress.")

    @contextmanager
    def start_activity(self, activity: str, time_limit: Optional[int] = None) -> Iterator[Stopwatch]:
        """ Mark the start of a new activity and automatically time its duration.
            TimeManager does not currently support nested activities. """
        with Stopwatch() as sw:
            self.current_activity = Activity(activity, sw, time_limit)
            self.activities.append(self.current_activity)
            yield sw
        self.current_activity = None
        log.info("{} took {:.4f}s.".format(activity, sw.elapsed_time))