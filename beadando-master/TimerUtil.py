import time

class timer_(object):
  def __init__(self):
    self._current_task = None
    self._timers = {}

    self._reftime = time.monotonic()


  # Elapsed time since the last reset.
  # Pass reset=True to reset elapsed time counter. nekünk false kell, A és B váltakozásánál az idő megáll.
  def _elapsed(self, reset=False):
    oldreftime = self._reftime
    newreftime = time.monotonic()
    if reset:
      self._reftime = newreftime

    return newreftime - oldreftime


  # Lekérdezi a jelenlegi task-ot
  def current_task(self):
    return self._current_task


  # Task-ot vált
  # returns the elapsed time from the current task (b4 switch)
  def switch_to(self, newtask):
    task = self._current_task
    elapsed = self._elapsed(True)
    if task is not None:
      self._timers[task] += elapsed

    self._current_task = newtask
    if newtask is not None and newtask not in self._timers:
      self._timers[newtask] = 0.0

    if task is not None:
      return self._timers[task]


  # Return the elapsed time for the specified task.
  # task=None to get the elapsed time for the current task.
  # reset=True to simultaneously reset the timer for this task.
  def elapsed_time(self, task=None, reset=False):
    if task is None:
      task = self._current_task
    if task not in self._timers:
      return None

    value = self._timers[task]
    if task == self._current_task:
      value += self._elapsed(reset)

    if reset:
      self._timers[task] = 0.0

    return value


  # Fetch all data points.
  # reset=True to simultaneously reset all timers.
  def all_elapsed_time(self, reset=False):
    values = self._timers.copy()
    elapsed = self._elapsed(reset)
    task = self._current_task
    if task is not None:
        values[task] += elapsed

    if reset:
      self._timers = {}
      if task is not None:
        self._timers[task] = 0.0

    return values