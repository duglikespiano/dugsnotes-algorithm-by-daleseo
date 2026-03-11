const strings = ['Hello', 'World', 'Yes:Or:No'];

function encoding(strings) {
	// 1. Encoding with a special delimiter
	// 0(n) time | 0(1) space
	// return strings.join('😆');
	//
	//
	// 2. Encode data with length information
	// 0(n) time | 0(1) space
	let text = '';
	for (const string of strings) {
		text += `${string.length}:${string}`;
	}

	return text;
}

function decoding(strings) {
	//  1. Decoding with a special delimiter
	//  0(n) time | 0(1) space
	// return strings.split('😆');
	//
	//
	// 2. Decode data with length information
	// 0(n) time | 0(1) space
	const array = [];
	let start = 0;
	while (start < strings.length) {
		const delimiterIndex = strings.indexOf(':', start);
		const stringLength = parseInt(strings.slice(start, delimiterIndex));
		const string = strings.slice(delimiterIndex + 1, delimiterIndex + 1 + stringLength);
		array.push(string);

		start = delimiterIndex + 1 + stringLength;
	}
	return array;
}

console.log(encoding(strings));
console.log(decoding(encoding(strings)));
