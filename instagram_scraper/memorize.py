def memorize(f):

    memo = {}

    def helper(self, *args, **kargs):

        if "DONT_USE_MEM" in kargs:
            dont = kargs.pop("DONT_USE_MEM")
        else:
            dont = False
            
        if self.DONT_USE_MEM or dont:
            return f(self, *args, **kargs)


        key = make_params_memory_name(*args, **kargs)
        if key not in memo:            
            memo[key] = f(self, *args, **kargs)

        return memo[key]

    return helper


def make_params_memory_name(*args, **kargs):
    s = ""
    for k,v in kargs.items():
        s += "{} : {},".format(k, str(v))

    for v in args:
        s += str(v) + ","
    return s