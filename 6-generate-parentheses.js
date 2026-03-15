function generateParentheses(n) {
	const result = [];
	const stack = [];

	function dfs(opening, closing) {
		if (opening === n && closing === n) {
			return result.push(stack.join(''));
		}
		if (opening < n) {
			stack.push('(');
			dfs(opening + 1, closing);
			stack.pop();
		}
		if (closing < opening) {
			stack.push(')');
			dfs(opening, closing + 1);
			stack.pop();
		}
	}

	dfs(0, 0);
	console.log(result);

	return result;
}

generateParentheses(3);
