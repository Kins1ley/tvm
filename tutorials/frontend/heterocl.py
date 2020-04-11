from . import config
from .schedule import Stage, Schedule
from .scheme import Scheme

def init(init_dtype="int32"):
    """Initialize a HeteroCL environment with configurations.

    This API must be called each time the users write an application.
    Within the same HeteroCL environment, users can try different
    combinations of customization primitives.

    Parameters
    ----------
    init_dtype : Type, optional
        The default data type for each variables

    Examples
    --------
    .. code-block:: python

        # app 1
        hcl.init()
        A = hcl.placeholder(...)
        B = hcl.placeholder(...)
        def app1(A, B):
            # define the algorithm for app 1
        s = hcl.create_scheme([A, B], app1)
        # apply customization primitives
        f1 = hcl.build(s)
        # execute f1

        # app 2 - initialize again with a different data type
        hcl.init(hcl.Float())
        A = hcl.placeholder(...)
        B = hcl.placeholder(...)
        C = hcl.placeholder(...)
        def app2(A, B, C):
            # define the algorithm for app 2
        s = hcl.create_scheme([A, B, C], app2)
        f2 = hcl.build(s)
        # execute f2
    """
    # set the configurations
    config.init_dtype = init_dtype
    # initialize global variables
    Schedule.stage_ops = []
    Schedule.last_stages = OrderedSet([])
    Scheme.current = None