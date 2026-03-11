function isValidParentheses(string) {
	const parens = { '(': ')', '{': '}', '[': ']' };
	const stack = [];

	for (const [index, character] of Array.from(string).entries()) {
		console.log(index, character);
		if (Object.hasOwn(parens, character)) {
			stack.push(character);
		} else {
			if (stack.length < 1 || character !== parens[stack.pop()]) {
				return false;
			}
		}
	}
	return stack.length < 1;
}

console.log(isValidParentheses('{([])}'));
console.log(isValidParentheses('{(})'));
