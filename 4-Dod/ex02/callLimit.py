def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function():
            nonlocal count
            nonlocal limit
            nonlocal function
            if count >= limit:
                print(
                    f"ERROR: <function {function.__name__} at {function}> call too many times.")
            else:
                count += 1
                function()
        return limit_function
    return callLimiter
