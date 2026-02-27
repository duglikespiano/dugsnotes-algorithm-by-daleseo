def generateParentheses(n):
    """
    (
      (
        ( ❌
        )
          ( ❌
          ) ✅ "(())"

      )
        (
          ( ❌
          ) ✅ "()()"
        ) ❌
    ) ❌

    0(2^n) time | 0(n^2) space
    """

    # result = []

    # def dfs(text, opening, closing):
    #     if opening == n and closing == n:
    #         return result.append(text)
    #     if opening > n or opening < closing:
    #         return
    #     dfs(text + "(", opening + 1, closing)
    #     dfs(text + ")", opening, closing + 1)

    # dfs("", 0, 0)

    """
    (
      (
        ) 
          ) ✅ "(())"

      )
        (          
          ) ✅ "()()"

    0(2^n) time | 0(n) space
    """
    result = []
    stack = []

    def dfs(opening, closing):
        if opening == n and closing == n:
            return result.append("".join(stack))
        if opening < n:
            stack.append("(")
            dfs(opening + 1, closing)
            stack.pop()
        if closing < opening:
            stack.append(")")
            dfs(opening, closing + 1)
            stack.pop()

    dfs(0, 0)

    print(result)

    return result


generateParentheses(3)
